from peewee import Model, CharField

from ..sqlite import sqlite_database


class Developer(Model):
    name = CharField()
    github_username = CharField()
    twitter_username = CharField()
    instagram_username = CharField()
    youtube_channel = CharField()

    class Meta:
        database = sqlite_database
