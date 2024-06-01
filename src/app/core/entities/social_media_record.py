from dataclasses import dataclass

from .entity import Entity


@dataclass
class SocialMediaRecord(Entity):
    github_followers_count = None
    twiter_followers_count = None
    instagram_followers_count = None
    youtube_subscribers_count = None

    github_repos_count = None
    github_stars_count = None

    instagram_posts_count = None
    instagram_likes_count = None

    twitter_retweets_count = None
    twitter_likes_count = None

    youtube_likes_count = None
    youtube_videos_count = None
