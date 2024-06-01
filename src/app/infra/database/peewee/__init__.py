from .sqlite import sqlite_database

from .models import DeveloperModel, SocialMediaRecordModel


class Peewee:
    def __init__(self) -> None:
        sqlite_database.connect()
        sqlite_database.create_tables([DeveloperModel, SocialMediaRecordModel])

        dev = DeveloperModel.get(DeveloperModel.id == 1)
        print(dev.name)
