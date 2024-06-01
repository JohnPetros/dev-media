from playhouse.shortcuts import model_to_dict

from ..models import SocialMediaRecordModel, DeveloperModel

from core.entities import SocialMediaRecord


class SocialMediaRecordsRepository:
    def get_last_by_developer_id(self, developer_id: int):
        try:
            record = (
                SocialMediaRecordModel.select()
                .join(DeveloperModel)
                .where(DeveloperModel.id == developer_id)
                .order_by(SocialMediaRecordModel.created_at.desc())
                .limit(1)
            ).first()

            return SocialMediaRecord(**model_to_dict(record))

        except Exception as exception:
            print(exception)
            return None

    def create(self, social_media_record: SocialMediaRecord, developer_id: int):
        SocialMediaRecordModel.create(
            github_followers_count=social_media_record.github_followers_count,
            github_stars_count=social_media_record.github_stars_count,
            github_repos_count=social_media_record.github_repos_count,
            instagram_followers_count=social_media_record.instagram_followers_count,
            instagram_likes_count=social_media_record.instagram_likes_count,
            instagram_posts_count=social_media_record.instagram_posts_count,
            twitter_followers_count=social_media_record.twitter_followers_count,
            twitter_likes_count=social_media_record.twitter_likes_count,
            twitter_retweets_count=social_media_record.twitter_retweets_count,
            youtube_subscribers_count=social_media_record.youtube_subscribers_count,
            youtube_likes_count=social_media_record.youtube_likes_count,
            developer=developer_id,
        )
