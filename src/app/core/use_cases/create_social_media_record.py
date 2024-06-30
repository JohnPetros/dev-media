from core.entities import SocialMediaRecord, Developer
from core.interfaces.providers import SocialMediaAPIProviderInterface
from core.interfaces.repositories import (
    SocialMediaRecordsRepositoryInterface,
    DevelopersRepositoryInterface,
)


class CreateSocialMediaRecord:
    def __init__(
        self,
        social_media_api: SocialMediaAPIProviderInterface,
        social_media_records_repository: SocialMediaRecordsRepositoryInterface,
        developers_repository: DevelopersRepositoryInterface,
    ):
        self.social_media_api = social_media_api
        self.social_media_records_repository = social_media_records_repository
        self.developers_repository = developers_repository

    def execute(self, developer_id: int):
        try:
            if not isinstance(developer_id, int):
                raise Exception("Developer id is not provided")

            developer = self.developers_repository.get_by_id(developer_id)

            if not isinstance(developer, Developer):
                raise Exception("Developer is not found")

            self.social_media_api.developer = developer
            social_media_data = self.social_media_api.fetch_data()

            social_media_record = SocialMediaRecord(
                developer=developer,
                **social_media_data,
            )

            self.social_media_records_repository.add(social_media_record)

            return social_media_record
        except Exception as exception:
            raise exception
