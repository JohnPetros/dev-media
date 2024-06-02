from peewee import Model as BaseModel

from ..postgresql import postgresql_database


class Model(BaseModel):
    class Meta:
        database = postgresql_database
