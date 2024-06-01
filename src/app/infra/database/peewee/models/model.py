from peewee import Model as BaseModel

from ..sqlite import sqlite_database


class Model(BaseModel):
    class Meta:
        database = sqlite_database
