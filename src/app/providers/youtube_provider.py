from os import getenv
from requests import get

from constants import SOCIAL_MEDIA


class YoutubeProvider:
    def __init__(self, channel_title) -> None:
        self.api_url = SOCIAL_MEDIA["youtube"]["api_url"]
        self.url = SOCIAL_MEDIA["youtube"]["url"]
        # self.api_key = getenv("YOUTUBE_API_KEY")
        self.api_key = "AIzaSyBqNYpiRxil082tSMRneE1A44v1T5hF8yg"
        self.channel_title = channel_title
        self.data = None

        try:
            channel_id = self.__fetch_channel_id()
            self.data = self.__fetch_channel_data(channel_id)

        except Exception as exeption:
            print("Youtube API Error: ", exeption)

    def get_followers_count(self):
        if self.data is None:
            return "Indisponível"

        return int(self.data["items"][0]["statistics"]["subscriberCount"])

    def get_link(self):
        return f"{self.url}/{self.channel_title}"

    def __fetch_channel_id(self):
        response = get(
            f"{self.api_url}/search?key={self.api_key}&part=snippet&q={self.channel_title}&type=video"
        )
        data = response.json()
        channel_id = data["items"][0]["snippet"]["channelId"]
        return channel_id

    def __fetch_channel_data(self, channel_id: str):
        response = get(
            f"{self.api_url}/channels?id={channel_id}&part=statistics&key={self.api_key}"
        )
        data = response.json()
        return data
