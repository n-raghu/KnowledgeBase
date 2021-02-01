from fastapi import FastAPI

from handlers import api_about
from handlers import api_addr_matcher

app = FastAPI()

app.include_router(
    api_about.api,
    prefix='/addr'
)
app.include_router(
    api_addr_matcher.api,
    prefix='/addr'
)
