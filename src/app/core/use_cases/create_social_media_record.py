from core.entities import SocialMediaRecord

from infra.database import developers_repository, social_media_records_repository
from infra.providers import SocialMediaApiProvider


class CreateSocialMediaRecord:
    def execute(self, developer_id: int):
        try:
            developer = developers_repository.get_by_id(developer_id)

            social_media_api = SocialMediaApiProvider(developer)
            social_media_data = social_media_api.fetch_data()

            social_media_record = SocialMediaRecord(
                developer=developer,
                **social_media_data,
            )

            social_media_records_repository.create(social_media_record, developer.id)
        except Exception as exception:
            raise exception
