from requests import get

from infra.constants import SOCIAL_MEDIA


class InstagramProvider:
    def __init__(self, username: str):
        self.api_url = SOCIAL_MEDIA["instagram"]["api_url"]
        self.url = SOCIAL_MEDIA["instagram"]["url"]
        self.username = username
        self.data = None

        try:
            headers = {
                "User-Agent": "Instagram 76.0.0.15.395 Android (24/7.0; 640dpi; 1440x2560; samsung; SM-G930F; herolte; samsungexynos8890; en_US; 138226743)"
            }

            response = get(f"{self.api_url}{self.username}", headers=headers)
            data = response.json()
            self.data = data

        except Exception as exeption:
            print("Instagram API Error: ", exeption)

    def get_followers_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["data"]["user"]["edge_followed_by"]["count"]

    def get_posts_count(self):
        if self.data is None:
            return "Indisponível"

        return self.data["data"]["user"]["edge_owner_to_timeline_media"]["count"]

    def get_likes_count(self):
        if self.data is None:
            return "Indisponível"

        count = 0
        for edge in self.data["data"]["user"]["edge_owner_to_timeline_media"]["edges"]:
            count += edge["node"]["edge_liked_by"]["count"]

        return count

    def get_link(self):
        return f"{self.url}/{self.username}"
