from requests import get

from constants import SOCIAL_MEDIA


class GithubProvider:
    def __init__(self, username) -> None:
        self.api_url = SOCIAL_MEDIA["github"]["api_url"]
        self.url = SOCIAL_MEDIA["github"]["url"]
        self.username = username
        self.data = None

        try:
            response = get(f"{self.api_url}/{self.username}")
            data = response.json()
            self.data = data

        except Exception as exeption:
            print("Github API Error: ", exeption)

    def get_followers_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["followers"]

    def get_link(self):
        return f"{self.url}/{self.username}"
