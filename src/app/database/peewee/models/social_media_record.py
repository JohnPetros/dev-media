from peewee import Model, DecimalField, ForeignKeyField

from ..sqlite import sqlite_database
from .developer import Developer


class SocialMediaRecord(Model):
    developer = ForeignKeyField(Developer, backref="developers")

    github_followers_count = DecimalField()
    twiter_followers_count = DecimalField()
    instagram_followers_count = DecimalField()
    youtube_subscribers_count = DecimalField()

    github_repositories_count = DecimalField()
    github_stars_count = DecimalField()

    instagram_posts_count = DecimalField()
    instagram_likes_count = DecimalField()

    twitter_retweets_count = DecimalField()
    twitter_likes_count = DecimalField()

    twitter_views_count = DecimalField()
    twitter_likes_count = DecimalField()

    class Meta:
        database = sqlite_database
