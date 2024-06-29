from core.entities import SocialMediaRecord, Developer
from core.interfaces.repositories import (
    DevelopersRepositoryInterface,
    SocialMediaRecordsRepositoryInterface,
)
from core.interfaces.providers import SocialMediaAPIProviderInterface


class GetPageData:
    def __init__(
        self,
        developers_repository: DevelopersRepositoryInterface,
        social_media_records_repository: SocialMediaRecordsRepositoryInterface,
        social_media_api: SocialMediaAPIProviderInterface,
    ):
        self.developers_repository = developers_repository
        self.social_media_records_repository = social_media_records_repository
        self.social_media_api = social_media_api

    def execute(self, developer_id: int):
        try:
            developer = self.developers_repository.get_by_id(developer_id)

            if not isinstance(developer, Developer):
                raise Exception("Developer not found")

            social_media_record = (
                self.social_media_records_repository.get_last_by_developer_id(
                    developer.id
                )
            )

            if not isinstance(social_media_record, SocialMediaRecord):
                self.social_media_api.developer = developer
                social_media_data = self.social_media_api.fetch_data()

                social_media_record = SocialMediaRecord(
                    developer=developer,
                    **social_media_data,
                )

                self.social_media_records_repository.add(social_media_record)

            return {
                "developer": developer,
                "social_media_record": social_media_record,
            }
        except Exception as exception:
            raise exception
