from ..models import SocialMediaRecordModel

from core.entities import SocialMediaRecord


class SocialMediaRecordsRepository:
    def get_all(self):
        return SocialMediaRecordModel.select()

    def create(self, social_media_record: SocialMediaRecord, developer_id: str):
        SocialMediaRecordModel.create(
            github_followers_count=social_media_record.github_followers_count,
            github_stars_count=social_media_record.github_stars_count,
            github_repos_count=social_media_record.github_repos_count,
            instagram_followers_count=social_media_record.instagram_followers_count,
            instagram_likes_count=social_media_record.instagram_likes_count,
            instagram_posts_count=social_media_record.instagram_posts_count,
            twiter_followers_count=social_media_record.twiter_followers_count,
            twitter_likes_count=social_media_record.twitter_likes_count,
            twitter_retweets_count=social_media_record.twitter_retweets_count,
            youtube_subscribers_count=social_media_record.youtube_subscribers_count,
            youtube_likes_count=social_media_record.youtube_likes_count,
            developer=developer_id,
        )
