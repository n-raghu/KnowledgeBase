import sys
from services.common import required_attributes


def ec2_instances(client) -> list:
    dat = client.describe_instances()
    ins_flds = required_attributes('instances')
    return [{fld: ins[fld] for fld in ins_flds} for ins in dat['Reservations'][0]['Instances']]


def img_info(client, images: list) -> dict:
    img_dat = client.describe_images(ImageIds=list(set(images)))['Images']
    img_flds = required_attributes('images')
    return {img['ImageId'] : {fld: img[fld] for fld in img_flds} for img in img_dat}
