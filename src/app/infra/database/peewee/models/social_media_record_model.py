from datetime import datetime, timezone

from peewee import CharField, ForeignKeyField, DateTimeField

from core.constants import DEFAULT_COUNT_VALUE

from .model import Model
from .developer_model import DeveloperModel


class SocialMediaRecordModel(Model):
    developer = ForeignKeyField(DeveloperModel, backref="social_media_records")

    github_followers_count = CharField(default=DEFAULT_COUNT_VALUE)
    twitter_followers_count = CharField(default=DEFAULT_COUNT_VALUE)
    instagram_followers_count = CharField(default=DEFAULT_COUNT_VALUE)
    youtube_subscribers_count = CharField(default=DEFAULT_COUNT_VALUE)

    github_repos_count = CharField(default=DEFAULT_COUNT_VALUE)
    github_stars_count = CharField(default=DEFAULT_COUNT_VALUE)

    instagram_posts_count = CharField(default=DEFAULT_COUNT_VALUE)
    instagram_likes_count = CharField(default=DEFAULT_COUNT_VALUE)

    twitter_retweets_count = CharField(default=DEFAULT_COUNT_VALUE)
    twitter_likes_count = CharField(default=DEFAULT_COUNT_VALUE)

    youtube_views_count = CharField(default=DEFAULT_COUNT_VALUE)
    youtube_videos_count = CharField(default=DEFAULT_COUNT_VALUE)

    created_at = DateTimeField(default=datetime.now(timezone.utc))

    class Meta:
        table_name = "social_media_records"
