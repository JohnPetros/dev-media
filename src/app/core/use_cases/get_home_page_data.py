from infra.database import developers_repository
from infra.providers import (
    GithubProvider,
    TwitterProvider,
    InstagramProvider,
    YoutubeProvider,
)
from core.helpers import format_count


class GetHomePageData:
    def execute(self, developer_id: int):
        developer = developers_repository.get_by_id(0)

        return {}

        github_data = self.__get_github_data(developer.github_username)
        twitter_data = self.__get_twitter_data(developer.twitter_username)
        instagram_data = self.__get_instagram_data(developer.instagram_username)
        youtube_data = self.__get_youtube_data(developer.youtube_channel)

        return {
            "developer": developer,
            **github_data,
            **twitter_data,
            **instagram_data,
            **youtube_data,
        }

    def __get_github_data(self, github_username: str):
        github_provider = GithubProvider(github_username)
        github_followers_count = github_provider.get_followers_count()
        github_link = github_provider.get_link()

        return {
            "github_followers_count": format_count(github_followers_count),
            "github_link": github_link,
        }

    def __get_twitter_data(self, twitter_username: str):
        twitter_provider = TwitterProvider(twitter_username)
        twitter_followers_count = twitter_provider.get_followers_count()
        twitter_link = twitter_provider.get_link()

        return {
            "twitter_followers_count": format_count(twitter_followers_count),
            "twitter_link": twitter_link,
        }

    def __get_instagram_data(self, instagram_username: str):
        instagram_provider = InstagramProvider(instagram_username)
        instagram_followers_count = instagram_provider.get_followers_count()
        instagram_link = instagram_provider.get_link()

        return {
            "instagram_followers_count": format_count(instagram_followers_count),
            "instagram_link": instagram_link,
        }

    def __get_youtube_data(self, youtube_channel: str):
        youtube_provider = YoutubeProvider(youtube_channel)
        youtube_followers_count = youtube_provider.get_followers_count()
        youtube_link = youtube_provider.get_link()

        return {
            "youtube_followers_count": format_count(youtube_followers_count),
            "youtube_link": youtube_link,
        }
