from datetime import datetime
from dataclasses import dataclass

from core.commons import Count

from .entity import Entity
from .developer import Developer


@dataclass
class SocialMediaRecord(Entity):
    github_followers_count: Count = None
    twitter_followers_count: Count = None
    instagram_followers_count: Count = None
    youtube_subscribers_count: Count = None

    github_repos_count: Count = None
    github_stars_count: Count = None

    instagram_posts_count: Count = None
    instagram_likes_count: Count = None

    twitter_retweets_count: Count = None
    twitter_likes_count: Count = None

    youtube_views_count: Count = None
    youtube_videos_count: Count = None

    created_at: datetime = None

    developer: Developer = None

    def __post_init__(self):
        self.github_followers_count = Count(self.github_followers_count)
        self.twitter_followers_count = Count(self.twitter_followers_count)
        self.instagram_followers_count = Count(self.instagram_followers_count)
        self.youtube_subscribers_count = Count(self.youtube_subscribers_count)

        self.github_repos_count = Count(self.github_repos_count)
        self.github_stars_count = Count(self.github_stars_count)

        self.instagram_posts_count = Count(self.instagram_posts_count)
        self.instagram_likes_count = Count(self.instagram_likes_count)

        self.twitter_retweets_count = Count(self.twitter_retweets_count)
        self.twitter_likes_count = Count(self.twitter_likes_count)

        self.youtube_views_count = Count(self.youtube_views_count)
        self.youtube_videos_count = Count(self.youtube_videos_count)
