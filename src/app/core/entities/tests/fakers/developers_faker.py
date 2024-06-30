from faker import Faker

from core.entities import Developer


class DevelopersFaker:
    @staticmethod
    def create():
        faker = Faker()

        return Developer(
            id=faker.random_int(),
            name=faker.name_male(),
            avatar_url=faker.url(),
            github_username=faker.user_name(),
            twitter_username=faker.user_name(),
            instagram_username=faker.user_name(),
            youtube_channel=faker.user_name(),
        )
