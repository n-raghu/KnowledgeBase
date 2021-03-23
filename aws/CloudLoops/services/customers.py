import sys

def get_customer_creds(customer):
    if customer == 'richardspark':
        return {
            'request': True,
            'key': 'AKIAYEL6T7E5CZFV5DGB',
            'secret': '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'
        }
    else:
        return {
            'request': False,
            'msg': f'Unknown Customer -{customer}'
        }
