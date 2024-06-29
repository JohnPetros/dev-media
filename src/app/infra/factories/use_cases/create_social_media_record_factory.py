from core.use_cases import CreateSocialMediaRecord

from infra.providers import SocialMediaApiProvider
from infra.database import developers_repository, social_media_records_repository


class CreateSocialMediaRecordFactory:
    @staticmethod
    def create():
        social_media_api_provider = SocialMediaApiProvider()
        return CreateSocialMediaRecord(
            social_media_records_repository=social_media_records_repository,
            developers_repository=developers_repository,
            social_media_api=social_media_api_provider,
        )
