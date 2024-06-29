from abc import ABC, abstractmethod

from core.entities import Developer


class DevelopersRepositoryInterface(ABC):
    @abstractmethod
    def get_by_id(self, id: int) -> Developer: ...

    @abstractmethod
    def add(self, developer: Developer) -> Developer: ...
