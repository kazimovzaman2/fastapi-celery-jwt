from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.users.model import User
from app.tasks.model import IPData

ALL_MODELS = [User, IPData]


def middlewareAPI(app: FastAPI, available=True):
    if available:
        app.add_middleware(
            CORSMiddleware,
            allow_origins="*",
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
