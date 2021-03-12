import sys
import json

import boto3

from essentials import get_svc_cfg, tree_traverse

cfg = get_svc_cfg()

filter_format: str = '[{{"Field": "tenancy", "Value": "{t}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "operatingSystem", "Value": "{o}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "preInstalledSw", "Value": "NA", "Type": "TERM_MATCH"}},'\
                '{{"Field": "instanceType", "Value": "{i}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "location", "Value": "{r}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "capacitystatus", "Value": "Used", "Type": "TERM_MATCH"}}]'

"""
t='shared', o='Linux', i='t3.large', r='US West (Oregon)'
"""


def convert_to_local_filters(doc: dict) -> dict:

    region = doc.get('region', False)
    os = doc.get('productDescription', False)

    if region == 'us-west-2':
        doc['region'] = 'US West (Oregon)'
    elif region == 'us-west-1':
        doc['region'] = 'US West (N. California)'

    if os == 'Linux/UNIX':
        doc['productDescription'] = 'Linux'

    return doc


def fetch_ec2_pricing(
    all_filters,
    fill_=filter_format
):
    imported_filters: dict = {filto['name']: filto['values'][0] for filto in all_filters}
    filters = convert_to_local_filters(imported_filters)

    fillers: list = json.loads(
        fill_.format(
            t=filters['tenancy'],
            o=filters['productDescription'],
            i=filters['instanceType'],
            r=filters['region']
        )
    )

    cfg = get_svc_cfg()
    pricing = boto3.client(
        'pricing',
        region_name='us-east-1',
        aws_access_key_id=cfg['key'],
        aws_secret_access_key=cfg['secret'],
    )

    response = pricing.get_products(
        ServiceCode='AmazonEC2',
        Filters=fillers
    )
    prices = response['PriceList']
    instances = json.loads(prices[0])

    return float(tree_traverse(instances, 'pricePerUnit')['USD'])
