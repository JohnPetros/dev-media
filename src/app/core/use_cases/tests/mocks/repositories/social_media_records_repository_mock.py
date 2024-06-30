from core.interfaces.repositories import SocialMediaRecordsRepositoryInterface
from core.entities import SocialMediaRecord


class SocialMediaRecordRepositoryMock(SocialMediaRecordsRepositoryInterface):
    _social_media_records: list[SocialMediaRecord] = []

    def get_last_by_developer_id(self, id: int):
        record = list(
            filter(lambda record: record.developer.id == id, self._social_media_records)
        )

        if not len(record):
            return None

        return record[-1]

    def get_from_yesterday(
        self,
        social_media_record: SocialMediaRecord,
    ) -> SocialMediaRecord:
        return social_media_record

    def add(self, social_media_record: SocialMediaRecord):
        self._social_media_records.append(social_media_record)
