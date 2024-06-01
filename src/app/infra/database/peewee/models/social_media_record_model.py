from peewee import DecimalField, ForeignKeyField

from core.constants import DEFAULT_COUNT_VALUE

from .model import Model
from .developer_model import DeveloperModel


class SocialMediaRecordModel(Model):
    developer = ForeignKeyField(DeveloperModel, backref="social_media_records")

    github_followers_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    twiter_followers_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    instagram_followers_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    youtube_subscribers_count = DecimalField(default=DEFAULT_COUNT_VALUE)

    github_repos_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    github_stars_count = DecimalField(default=DEFAULT_COUNT_VALUE)

    instagram_posts_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    instagram_likes_count = DecimalField(default=DEFAULT_COUNT_VALUE)

    twitter_retweets_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    twitter_likes_count = DecimalField(default=DEFAULT_COUNT_VALUE)

    youtube_likes_count = DecimalField(default=DEFAULT_COUNT_VALUE)
    youtube_videos_count = DecimalField(default=DEFAULT_COUNT_VALUE)
