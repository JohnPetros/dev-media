from datetime import datetime

from core.entities.tests.fakers import SocialMediaRecordsFaker


def describe_social_media_record_entity():
    def it_should_get_total_followers_count():
        fake_social_media_record = SocialMediaRecordsFaker.create(
            github_followers_count="10",
            instagram_followers_count="10",
            twitter_followers_count="10",
            youtube_subscribers_count="10",
        )

        total_count = fake_social_media_record.get_total_followers_count()

        assert total_count.get_value() == "40"

    def it_should_format_created_at_to_datetime_if_it_is_string():
        fake_social_media_record = SocialMediaRecordsFaker.create(
            created_at="2024-07-01 09:00:00"
        )

        assert isinstance(fake_social_media_record.created_at, datetime)
