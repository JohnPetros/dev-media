from peewee import CharField

from .model import Model


class DeveloperModel(Model):
    name = CharField()
    github_username = CharField()
    twitter_username = CharField()
    instagram_username = CharField()
    youtube_channel = CharField()
    avatar_url = CharField()

    class Meta:
        table_name = "developers"
