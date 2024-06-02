from core.entities import Developer

from ..models import DeveloperModel


class DevelopersRepository:
    def get_by_id(self, id: int):
        try:
            row = DeveloperModel.get(id)

            return self.__get_developer_instace(row)
        except Exception:
            print(f"Get Developer By Id Error: {row}")
            return None

    def __get_developer_instace(self, model: DeveloperModel):
        return Developer(
            id=model.id,
            name=model.name,
            github_username=model.github_username,
            twitter_username=model.twitter_username,
            instagram_username=model.instagram_username,
            youtube_channel=model.youtube_channel,
            avatar_url=model.avatar_url,
        )
