from faker import Faker

from core.entities import SocialMediaRecord

from .developers_faker import DevelopersFaker


class SocialMediaRecordsFaker:
    _record: SocialMediaRecord = None

    @classmethod
    def create(cls, **record: SocialMediaRecord):
        faker = Faker()

        if record is not None:
            cls._record = record

        return SocialMediaRecord(
            id=cls.__set_value("github_repos_count", faker.random_int()),
            github_repos_count=cls.__set_value(
                "github_repos_count", str(faker.random_int())
            ),
            github_stars_count=cls.__set_value(
                "github_stars_count", str(faker.random_int())
            ),
            github_followers_count=cls.__set_value(
                "github_followers_count", str(faker.random_int())
            ),
            twitter_likes_count=cls.__set_value(
                "twitter_likes_count", str(faker.random_int())
            ),
            twitter_followers_count=cls.__set_value(
                "twitter_followers_count",
                str(faker.random_int()),
            ),
            twitter_retweets_count=cls.__set_value(
                "twitter_retweets_count", str(faker.random_int())
            ),
            instagram_posts_count=cls.__set_value(
                "instagram_posts_count", str(faker.random_int())
            ),
            instagram_likes_count=cls.__set_value(
                "instagram_likes_count", str(faker.random_int())
            ),
            instagram_followers_count=cls.__set_value(
                "instagram_followers_count", str(faker.random_int())
            ),
            youtube_subscribers_count=cls.__set_value(
                "youtube_subscribers_count", str(faker.random_int())
            ),
            youtube_videos_count=cls.__set_value(
                "youtube_videos_count", str(faker.random_int())
            ),
            youtube_views_count=cls.__set_value(
                "youtube_views_count", str(faker.random_int())
            ),
            created_at=cls.__set_value("created_at", faker.date("%Y-%m-%d %H:%M:%S")),
            developer=cls.__set_value("developer", DevelopersFaker.create()),
        )

    @classmethod
    def __set_value(cls, attribute: str, fallback):
        if attribute in cls._record:
            return cls._record[attribute]
        else:
            return fallback
