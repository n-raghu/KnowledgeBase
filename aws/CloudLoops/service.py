from fastapi import FastAPI

from handlers import api_capture_customer_info

app = FastAPI(
    title="CloudLoops",
    description='Smart Cloud Management',
    version='0.1',
)

app.include_router(
    api_capture_customer_info.router,
)
