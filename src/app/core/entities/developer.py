from dataclasses import dataclass

from .entity import Entity


@dataclass
class Developer(Entity):
    name = None
    github_username = None
    twitter_username = None
    instagram_username = None
    youtube_channel = None
