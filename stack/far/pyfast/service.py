import sys
from datetime import datetime as dtm

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

api.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get('/')
async def root() -> dict:
    return {
        "svc": "React with FastAPI",
        "time_utc": dtm.utcnow(),
        "time_local": dtm.now()
    }
