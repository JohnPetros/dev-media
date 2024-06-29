from datetime import timedelta

from playhouse.shortcuts import model_to_dict

from ..models import SocialMediaRecordModel, DeveloperModel

from core.entities import SocialMediaRecord, Developer


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

            if not record:
                return None

            return self.__get_social_media_record_instance(record)

        except Exception as exception:
            print(exception)
            return None

    def get_from_yesterday(self, social_media_record: SocialMediaRecord):
        try:
            yesterday_datetime = social_media_record.created_at - timedelta(minutes=1)

            record = (
                SocialMediaRecordModel.select()
                .join(DeveloperModel)
                .where(
                    (DeveloperModel.id == social_media_record.developer.id)
                    & (SocialMediaRecordModel.created_at <= yesterday_datetime)
                )
                .order_by(SocialMediaRecordModel.created_at)
                .limit(1)
            ).first()

            if not record:
                return None

            return self.__get_social_media_record_instance(record)

        except Exception as exception:
            print("exception", exception)
            return None

    def add(self, social_media_record: SocialMediaRecord, developer_id: int):
        SocialMediaRecordModel.create(
            github_followers_count=social_media_record.github_followers_count.get_value(),
            github_stars_count=social_media_record.github_stars_count.get_value(),
            github_repos_count=social_media_record.github_repos_count.get_value(),
            instagram_followers_count=social_media_record.instagram_followers_count.get_value(),
            instagram_likes_count=social_media_record.instagram_likes_count.get_value(),
            instagram_posts_count=social_media_record.instagram_posts_count.get_value(),
            twitter_followers_count=social_media_record.twitter_followers_count.get_value(),
            twitter_likes_count=social_media_record.twitter_likes_count.get_value(),
            twitter_retweets_count=social_media_record.twitter_retweets_count.get_value(),
            youtube_subscribers_count=social_media_record.youtube_subscribers_count.get_value(),
            youtube_views_count=social_media_record.youtube_views_count.get_value(),
            youtube_videos_count=social_media_record.youtube_videos_count.get_value(),
            developer=developer_id,
        )

    def __get_social_media_record_instance(self, model: SocialMediaRecordModel):
        developer = Developer(**model_to_dict(model.developer))

        model_dict = model_to_dict(model)
        del model_dict["developer"]

        return SocialMediaRecord(developer=developer, **model_dict)
