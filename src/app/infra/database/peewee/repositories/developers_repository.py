from core.entities import Developer

from ..models import DeveloperModel


class DevelopersRepository:
    def get_by_id(self, id: int):
        try:
            row = DeveloperModel.get(id)

            developer = Developer(
                id=row.id,
                name=row.name,
                github_username=row.github_username,
                twitter_username=row.twitter_username,
                instagram_username=row.instagram_username,
                youtube_channel=row.youtube_channel,
                avatar_url=row.avatar_url,
            )

            return developer
        except Exception:
            return None
