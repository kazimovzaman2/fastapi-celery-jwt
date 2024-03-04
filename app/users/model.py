from app.config.database import BaseModel
from peewee import CharField


class User(BaseModel):
    first_name = CharField(unique=True)
    last_name = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
