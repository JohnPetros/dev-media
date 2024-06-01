from datetime import datetime
from dataclasses import dataclass

from .entity import Entity
from .developer import Developer


@dataclass
class SocialMediaRecord(Entity):
    github_followers_count: int = None
    twitter_followers_count: int = None
    instagram_followers_count: int = None
    youtube_subscribers_count: int = None

    github_repos_count: int = None
    github_stars_count: int = None

    instagram_posts_count: int = None
    instagram_likes_count: int = None

    twitter_retweets_count: int = None
    twitter_likes_count: int = None

    youtube_views_count: int = None
    youtube_videos_count: int = None

    created_at: datetime = None

    developer: Developer = None
