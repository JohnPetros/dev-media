from requests import get

from infra.constants import SOCIAL_MEDIA


class GithubProvider:
    def __init__(self, username) -> None:
        self.api_url = SOCIAL_MEDIA["github"]["api_url"]
        self.url = SOCIAL_MEDIA["github"]["url"]
        self.client_id = "00846d991c108086334f"
        self.client_secret = "70790f0f99edc910a3b36767dbc9d18ccbd0e4de"

        self.username = username
        self.data = None

        try:
            response = get(f"{self.api_url}/{self.username}?{self.__get_credencials()}")
            data = response.json()

            if "message" in data and "authenticated" in data["message"].lower():
                raise Exception("Authenticated")

            self.data = data

        except Exception as exception:
            print("Github API Error: ", exception)

    def get_followers_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["followers"]

    def get_repos_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["public_repos"]

    def get_stars_count(self):
        try:
            response = get(
                f"https://api.github-star-counter.workers.dev/user/{self.username}"
            )
            data = response.json()
            return data["stars"]

        except Exception as exception:
            print("Github API Error: ", exception)
            return "Indisponível"

    def get_link(self):
        return f"{self.url}/{self.username}"

    def __get_credencials(self):
        return f"client_id={self.client_id}&client_secret={self.client_secret}"
