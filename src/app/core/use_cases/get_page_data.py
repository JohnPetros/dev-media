from core.entities import SocialMediaRecord, Developer

from infra.database import developers_repository, social_media_records_repository
from infra.providers import SocialMediaApiProvider


class GetPageData:
    def execute(self, developer_id: int):
        try:
            developer = developers_repository.get_by_id(developer_id)

            if not isinstance(developer, Developer):
                raise Exception("Developer not found")

            social_media_record = (
                social_media_records_repository.get_last_by_developer_id(developer.id)
            )

            if not isinstance(social_media_record, SocialMediaRecord):
                social_media_api = SocialMediaApiProvider(developer)
                social_media_data = social_media_api.fetch_data()

                social_media_record = SocialMediaRecord(
                    developer=developer,
                    **social_media_data,
                )

                social_media_records_repository.create(
                    social_media_record, developer.id
                )

            return {
                "developer": developer,
                "social_media_record": social_media_record,
            }
        except Exception as exception:
            raise exception
