from ..models import DeveloperModel


class DevelopersRepository:
    def get_by_id(self, id: int):
        return DeveloperModel.select(id)
