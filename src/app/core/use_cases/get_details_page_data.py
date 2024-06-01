from infra.database import developers_repository
from infra.providers import (
    GithubProvider,
    TwitterProvider,
    InstagramProvider,
    YoutubeProvider,
)
from core.helpers import format_count


class GetDetailsPageData:
    def execute(self, developer_id: str):
        developer = developers_repository.get_by_id(developer_id)

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
        github_repos_count = github_provider.get_repos_count()
        github_stars_count = github_provider.get_stars_count()

        return {
            "github_followers_count": format_count(github_followers_count),
            "github_repos_count": format_count(github_repos_count),
            "github_stars_count": format_count(github_stars_count),
        }

    def __get_twitter_data(self, twitter_username: str):
        twitter_provider = TwitterProvider(twitter_username)
        twitter_followers_count = twitter_provider.get_followers_count()
        twitter_likes_count = twitter_provider.get_likes_count()
        twitter_retweets_count = twitter_provider.get_retweets_count()

        return {
            "twitter_followers_count": format_count(twitter_followers_count),
            "twitter_likes_count": format_count(twitter_likes_count),
            "twitter_retweets_count": format_count(twitter_retweets_count),
        }

    def __get_instagram_data(self, instagram_username: str):
        instagram_provider = InstagramProvider(instagram_username)
        instagram_followers_count = instagram_provider.get_followers_count()
        instagram_posts_count = instagram_provider.get_posts_count()
        instagram_likes_count = instagram_provider.get_likes_count()

        return {
            "instagram_followers_count": format_count(instagram_followers_count),
            "instagram_posts_count": format_count(instagram_posts_count),
            "instagram_likes_count": format_count(instagram_likes_count),
        }

    def __get_youtube_data(self, youtube_channel: str):
        youtube_provider = YoutubeProvider(youtube_channel)
        youtube_followers_count = youtube_provider.get_followers_count()

        return {
            "youtube_followers_count": format_count(youtube_followers_count),
        }
