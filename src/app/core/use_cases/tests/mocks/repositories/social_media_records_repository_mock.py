from core.interfaces.repositories import SocialMediaRecordsRepositoryInterface
from core.entities import SocialMediaRecord


class SocialMediaRecordRepositoryMock(SocialMediaRecordsRepositoryInterface):
    _social_media_records: list[SocialMediaRecord] = []

    def get_last_by_developer_id(self, id: int):
        developer = list(
            filter((lambda developer: developer.id == id, self._social_media_records))
        )[0]

        return developer

    def add(self, social_media_record: SocialMediaRecord):
        self._social_media_records.append(social_media_record)
