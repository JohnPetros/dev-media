from abc import ABC, abstractmethod

from core.entities import Developer


class SocialMediaAPIProviderInterface(ABC):
    @property
    def developer(self) -> Developer: ...

    @developer.setter
    def developer(self, new_developer: Developer) -> Developer: ...

    @abstractmethod
    def fetch_data(self) -> dict: ...
