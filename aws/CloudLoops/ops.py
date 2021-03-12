import sys

import boto3
from fastapi import APIRouter

key = 'AKIAYEL6T7E5GKDJRKPD'
region = 'us-west-2'
secret = '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'


filter_format = '[{{"Field": "tenancy", "Value": "shared", "Type": "TERM_MATCH"}},'\
                '{{"Field": "operatingSystem", "Value": "{o}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "preInstalledSw", "Value": "NA", "Type": "TERM_MATCH"}},'\
                '{{"Field": "instanceType", "Value": "{t}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "location", "Value": "{r}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "capacitystatus", "Value": "Used", "Type": "TERM_MATCH"}}]'

filter_format = '[{{"Field": "tenancy", "Value": "shared", "Type": "TERM_MATCH"}},'\
                '{{"Field": "operatingSystem", "Value": "{o}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "preInstalledSw", "Value": "NA", "Type": "TERM_MATCH"}},'\
                '{{"Field": "instanceType", "Value": "{t}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "location", "Value": "{r}", "Type": "TERM_MATCH"}},'\
                '{{"Field": "capacitystatus", "Value": "UnusedCapacityReservation", "Type": "TERM_MATCH"}}]'


def get_ec2_instances(client) -> list:
    dat = client.describe_instances()
    ins_flds = required_attributes('instances')
    return [{fld: ins[fld] for fld in ins_flds} for ins in dat['Reservations'][0]['Instances']]


def required_attributes(resource) -> list:
    if resource == 'instances':
        return ['ImageId', 'InstanceId', 'InstanceType', 'LaunchTime', 'Architecture']
    if resource == 'images':
        return ['PlatformDetails', 'Name', 'RootDeviceType']


def get_img_info(client, images: list) -> dict:
    img_dat = client.describe_images(ImageIds=list(set(images)))['Images']
    img_flds = required_attributes('images')
    return {img['ImageId'] : {fld: img[fld] for fld in img_flds} for img in img_dat}


def refresh_cnx(resource, ctype='client', region=region):
    if ctype == 'client':
        return boto3.client(
            resource,
            region_name=region,
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )
    elif ctype == 'resource':
        return boto3.resource(
            resource,
            region_name=region,
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )
    else:
        print('Unknown CNX')


def tree_traverse(tree, key):
    for k, v  in tree.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            found = tree_traverse(v, key) 
            if found is not None:  # check if recursive call found it
                return found
