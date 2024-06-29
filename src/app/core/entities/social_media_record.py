from datetime import datetime
from dataclasses import dataclass

from core.structs import Count

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

        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(
                self.created_at[:19], "%Y-%m-%d %H:%M:%S"
            )

    def get_total_followers_count(self):
        total_count = 0

        for count in [
            self.github_followers_count.get_value(),
            self.twitter_followers_count.get_value(),
            self.instagram_followers_count.get_value(),
            self.youtube_subscribers_count.get_value(),
        ]:
            if count.isnumeric():
                total_count += int(count)

        return Count(str(total_count))
