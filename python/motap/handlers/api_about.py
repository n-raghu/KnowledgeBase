from datetime import datetime as dtm

from yaml import safe_load
from fastapi import APIRouter

with open('config.yml') as yfile:
    cfg = safe_load(yfile)

api = APIRouter()
hosted = dtm.utcnow()
rsc = cfg['resources']['about']

@api.get(rsc)
def api_about():
    return {
        "service": "Address Matcher",
        "hosted_at": f'{hosted} UTC'
    }
