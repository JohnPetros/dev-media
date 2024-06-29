from core.interfaces.providers import SocialMediaAPIProviderInterface


class SocialMediaApiProviderMock(SocialMediaAPIProviderInterface):
    def fetch_data(self):
        return {}
