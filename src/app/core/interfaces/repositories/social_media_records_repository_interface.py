from abc import ABC, abstractmethod

from core.entities import SocialMediaRecord


class SocialMediaRecordsRepositoryInterface(ABC):
    @abstractmethod
    def get_last_by_developer_id(
        self, developer_id: int
    ) -> SocialMediaRecord | None: ...

    @abstractmethod
    def get_from_yesterday(
        self, social_media_record: SocialMediaRecord
    ) -> SocialMediaRecord: ...
