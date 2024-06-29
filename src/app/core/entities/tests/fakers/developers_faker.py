from faker import Faker

from core.entities import Developer


class DevelopersFaker:
    def __init__(self):
        self.faker = Faker()

    @staticmethod
    def create(self):
        return Developer(
            id=self.faker.random_int(),
            name=self.faker.name_male(),
            avatar_url=self.faker.url(),
            github_username=self.faker.user_name(),
            youtube_channel=self.faker.user_name(),
            instagram_username=self.faker.user_name(),
            twitter_username=self.faker.user_name(),
        )

    @staticmethod
    def create_many(self, count: int = 10):
        return [self.create() for _ in range(count)]
