from datetime import datetime as dtm
from dateutil.relativedelta import relativedelta

from yaml import safe_load
from fuzzywuzzy import fuzz
from fastapi import APIRouter

from schemamodels import AddrSchema

with open('config.yml') as yfile:
    cfg = safe_load(yfile)

api = APIRouter()
rsc = cfg['resources']['addressmatcher']


def calculate_loan_amount(req_doc):
    headroom = req_doc.income * (req_doc.allowedFoir / 100) - req_doc.existingEMI
    amount = headroom * req_doc.loanTenure
    if amount < 10000:
        return False
    _a100 = amount % 100
    loanAmount = amount if not _a100 else amount - _a100
    return int(loanAmount) if loanAmount < 500_000 else 500_000


def consumer_input_validations_failed(requisites, req_doc):
    age = relativedelta(
        dtm.utcnow(),
        dtm.strptime(req_doc.dob, '%d/%m/%Y')
    ).years
    if not requisites['age']['min'] < age < requisites['age']['max']:
        return "Age not met"
    elif req_doc.income < requisites['income']:
        return "Low Income"
    elif req_doc.bureauScore < requisites['bureauScore']:
        return "Low Bureau Score"
    elif req_doc.applicationScore < requisites['applicationScore']:
        return 'Low Application Score'
    elif req_doc.maxDelL12M > requisites['maxDelL12M']:
        return 'maxDelL12M'
    return False


@api.get(rsc)
def api_matcher(req_body: AddrSchema):
    consumer_requisites = cfg['consumer_requisites']
    failed_validations = consumer_input_validations_failed(consumer_requisites, req_body)
    if failed_validations:
        req_body.rejected = failed_validations
        return req_body

    ratio = fuzz.token_set_ratio(str(req_body.currentAddress).lower(), str(req_body.bureauAddress).lower())
    req_body.address_matched = ratio

    """
    {
        'token_set': fuzz.token_set_ratio(str(req_body.currentAddress).lower(), str(req_body.bureauAddress).lower()),
        'token_sort': fuzz.token_sort_ratio(str(req_body.currentAddress).lower(), str(req_body.bureauAddress).lower()),
        'partial_ratio': fuzz.partial_ratio(str(req_body.currentAddress).lower(), str(req_body.bureauAddress).lower()),
        'ratio': fuzz.ratio(str(req_body.currentAddress).lower(), str(req_body.bureauAddress).lower()),
    }
    """

    if ratio < 80:
        req_body.rejected = "Address not close"
        return req_body
    loan_amount = calculate_loan_amount(req_body)
    req_body.loanAmount = loan_amount
    req_body.rejected = False if loan_amount else "Loan Amount Rejected"
    return req_body
