from faker import Faker

from core.interfaces.providers import SocialMediaAPIProviderInterface


class SocialMediaApiProviderMock(SocialMediaAPIProviderInterface):
    def __init__(self):
        faker = Faker()

        self.fake_social_media_record = {
            "github_repos_count": str(faker.random_int()),
            "github_stars_count": str(faker.random_int()),
            "github_followers_count": str(faker.random_int()),
            "twitter_likes_count": str(faker.random_int()),
            "twitter_followers_count": str(faker.random_int()),
            "twitter_retweets_count": str(faker.random_int()),
            "instagram_posts_count": str(faker.random_int()),
            "instagram_likes_count": str(faker.random_int()),
            "instagram_followers_count": str(faker.random_int()),
            "youtube_subscribers_count": str(faker.random_int()),
            "youtube_videos_count": str(faker.random_int()),
            "youtube_views_count": str(faker.random_int()),
        }

    def fetch_data(self):
        return self.fake_social_media_record
