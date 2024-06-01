from dataclasses import dataclass

from .entity import Entity


@dataclass
class Developer(Entity):
    name: str = None
    github_username: str = None
    twitter_username: str = None
    instagram_username: str = None
    youtube_channel: str = None
    avatar_url: str = None
