import sys

import boto3
from fastapi import APIRouter
from yaml import safe_load_all
from fastapi import HTTPException

from essentials import get_svc_cfg
from services.sps import estimate_savings
from services.customers import get_customer_creds
from services.ec2 import ec2_instances, img_info

router = APIRouter()


@router.get('/v1/ec2/analyze')
async def ec2_analyzer(
    customer: str,
    commission: float = 0.36,
    upfront: str = 'full',
    period: str = 'long',
    dry: bool = False,
):
    cfg = get_svc_cfg()
    cc = get_customer_creds(customer)
    if not cc['request']:
        raise HTTPException(
            status_code=404,
            detail=cc
    )
    cln_ec2 = boto3.client(
        'ec2',
        region_name=cfg['region'],
        aws_access_key_id=cc['key'],
        aws_secret_access_key=cc['secret'],
    )
    ec2_dat = []
    ins_dat = ec2_instances(cln_ec2)
    all_images = [ins['ImageId'] for ins in ins_dat]
    img_dat = img_info(cln_ec2, all_images)
    for ins in ins_dat:
        ins['image_info'] = img_dat[ins['ImageId']]
        x_estimates = estimate_savings(
            commission=commission,
            period=period,
            upfront=upfront,
            sp='EC2Instance',
            svc='EC2',
            product_desc=ins['image_info']['PlatformDetails'],
            region=cfg['region'],
            tenancy='shared',
            itype=ins['InstanceType'] if not dry else 't3.large',
        )
        ins['estimates'] = x_estimates
        ec2_dat.append(ins)

    return ec2_dat
