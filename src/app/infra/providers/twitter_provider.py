from requests import get

from infra.constants import SOCIAL_MEDIA


class TwitterProvider:
    def __init__(self, username: str):
        self.api_url = SOCIAL_MEDIA["twitter"]["api_url"]
        self.url = SOCIAL_MEDIA["twitter"]["url"]
        self.username = username
        self.data = None

        try:
            response = get(f"{self.api_url}/{self.username}")
            data = response.json()
            self.data = data

        except Exception as exeption:
            print("Twitter API Error: ", exeption)

    def get_followers_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["followersCount"]

    def get_retweets_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["statusesCount"]

    def get_likes_count(self):
        if self.data is None:
            return "Indisponível"

        return int(self.data["likeCount"])

    def get_link(self):
        return f"{self.url}/{self.username}"
