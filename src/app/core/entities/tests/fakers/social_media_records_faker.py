from faker import Faker

from core.entities import SocialMediaRecord

from .developers_faker import DevelopersFaker


class SocialMediaRecordsFaker:
    @staticmethod
    def create():
        faker = Faker()

        return SocialMediaRecord(
            id=faker.random_int(),
            github_repos_count=str(faker.random_int()),
            github_stars_count=str(faker.random_int()),
            github_followers_count=str(faker.random_int()),
            twitter_likes_count=str(faker.random_int()),
            twitter_followers_count=str(faker.random_int()),
            twitter_retweets_count=str(faker.random_int()),
            instagram_posts_count=str(faker.random_int()),
            instagram_likes_count=str(faker.random_int()),
            instagram_followers_count=str(faker.random_int()),
            youtube_subscribers_count=str(faker.random_int()),
            youtube_videos_count=str(faker.random_int()),
            youtube_views_count=str(faker.random_int()),
            created_at=faker.date("%Y-%m-%d %H:%M:%S"),
            developer=DevelopersFaker.create(),
        )

    @staticmethod
    def create_many(count: int = 10):
        return [SocialMediaRecordsFaker.create() for _ in range(count)]
