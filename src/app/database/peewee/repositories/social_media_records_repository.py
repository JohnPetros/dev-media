from ..models import SocialMediaRecord


class SocialMediaRecordsRepository:
    def get_all(self):
        return SocialMediaRecord.select()
