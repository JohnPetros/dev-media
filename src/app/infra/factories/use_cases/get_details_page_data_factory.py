from core.use_cases import GetDetailsPageData

from infra.database import social_media_records_repository


class GetDetailsPageDataFactory:
    @staticmethod
    def create():
        return GetDetailsPageData(
            social_media_records_repository=social_media_records_repository
        )
