import sys

def get_customer_creds(customer):
    if customer == 'richardspark':
        return {
            'request': True,
            'key': 'AKIAYEL6T7E5GKDJRKPD',
            'secret': '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'
        }
    else:
        return {
            'request': False,
            'msg': f'Unknown Customer -{customer}'
        }
