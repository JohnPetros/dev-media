from core.entities import Developer

from .github_provider import GithubProvider
from .twitter_provider import TwitterProvider
from .instagram_provider import InstagramProvider
from .youtube_provider import YoutubeProvider


class SocialMediaApiProvider:
    def __init__(self, developer: Developer):
        try:
            if not isinstance(developer, Developer):
                raise Exception("Developer is not provided")

            self.developer = developer
        except Exception as exception:
            raise exception

    def fetch_data(self):
        github_data = self.__get_github_data(self.developer.github_username)
        twitter_data = self.__get_twitter_data(self.developer.twitter_username)
        instagram_data = self.__get_instagram_data(self.developer.instagram_username)
        youtube_data = self.__get_youtube_data(self.developer.youtube_channel)

        return {
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
            "github_followers_count": github_followers_count,
            "github_repos_count": github_repos_count,
            "github_stars_count": github_stars_count,
        }

    def __get_twitter_data(self, twitter_username: str):
        twitter_provider = TwitterProvider(twitter_username)
        twitter_followers_count = twitter_provider.get_followers_count()
        twitter_likes_count = twitter_provider.get_likes_count()
        twitter_retweets_count = twitter_provider.get_retweets_count()

        return {
            "twitter_followers_count": twitter_followers_count,
            "twitter_likes_count": twitter_likes_count,
            "twitter_retweets_count": twitter_retweets_count,
        }

    def __get_instagram_data(self, instagram_username: str):
        instagram_provider = InstagramProvider(instagram_username)
        instagram_followers_count = instagram_provider.get_followers_count()
        instagram_posts_count = instagram_provider.get_posts_count()
        instagram_likes_count = instagram_provider.get_likes_count()

        return {
            "instagram_followers_count": instagram_followers_count,
            "instagram_posts_count": instagram_posts_count,
            "instagram_likes_count": instagram_likes_count,
        }

    def __get_youtube_data(self, youtube_channel: str):
        youtube_provider = YoutubeProvider(youtube_channel)
        youtube_subscribers_count = youtube_provider.get_subscribers_count()

        return {
            "youtube_subscribers_count": youtube_subscribers_count,
        }
