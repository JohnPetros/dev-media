from core.interfaces.repositories import DevelopersRepositoryInterface
from core.entities import Developer


class DevelopersRepositoryMock(DevelopersRepositoryInterface):
    _developers: list[Developer] = []

    def get_by_id(self, id: int):
        developer = list(filter(lambda developer: developer.id == id, self._developers))

        if not len(developer):
            return []

        return developer[0]

    def add(self, developer: Developer):
        self._developers.append(developer)
