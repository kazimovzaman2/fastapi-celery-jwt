from app.config.database import BaseModel
from peewee import CharField, FloatField


class IPData(BaseModel):
    ip = CharField()
    country_name = CharField()
    latitude = FloatField()
    longitude = FloatField()
    flag = CharField()
    continent_code = CharField()
