import sys

import boto3

from essentials import get_svc_cfg
from services.pricing import fetch_ec2_pricing

cfg = get_svc_cfg()


def calculate_xpenses(
    commission: float,
    discount_rate: float,
    demand_rate: float
):
    demand_rate_per_day = 24 * demand_rate
    discount_rate_per_day = 24 * discount_rate
    commission_per_day = (1 - commission) * (demand_rate_per_day - discount_rate_per_day)
    provider_offer_day = discount_rate_per_day + commission_per_day
    return {
        "commission": commission,
        "PresentDailyExpense": round(demand_rate_per_day, 1),
        "ProviderDailyEstimate": round(provider_offer_day, 1),
        "PresentMonthlyExpense": round(31 * demand_rate_per_day, 1),
        "ProviderMonthlyEstimate": round(31 * provider_offer_day, 1),
    }


def estimate_savings(
    commission,
    period,
    upfront,
    sp,
    svc,
    product_desc,
    region,
    tenancy,
    itype,
    cfg=cfg,
):
    aws_tenancy = 'shared' if tenancy in ['shared', 'default'] else 'dedicated'
    duration = 94608000 if period == 'long' else 31536000

    client = boto3.client(
        'savingsplans',
        region_name=region,
        aws_access_key_id=cfg['key'],
        aws_secret_access_key=cfg['secret']
    )

    if upfront == 'full':
        aws_upfront = 'All Upfront'
    elif upfront == 'partial':
        aws_upfront = 'Partial Upfront'
    elif upfront == 'no':
        aws_upfront = 'No Upfront'
    else:
        raise "Unknown upfront value"

    filto = [
        {'name': 'instanceType', 'values': [itype]},
        {'name': 'tenancy', 'values': [aws_tenancy]},
        {'name': 'region', 'values': [region]},
        {'name': 'productDescription', 'values': [product_desc]},
    ]

    client_dat = client.describe_savings_plans_offering_rates(
        usageTypes=[f'USW2-UnusedBox:{itype}'],
        savingsPlanPaymentOptions=[aws_upfront],
        savingsPlanTypes=[sp],
        filters=filto
    )['searchResults']
    ec2_match = [doc for doc in client_dat if doc['savingsPlanOffering']['durationSeconds'] == duration][0]
    print(ec2_match)
    return calculate_xpenses(
        commission=commission,
        discount_rate=float(ec2_match['rate']),
        demand_rate=fetch_ec2_pricing(filto)
    )
