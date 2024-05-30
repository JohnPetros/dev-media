from ..models import Developer


class DevelopersRepository:
    def get_by_id(self, id: str):
        return Developer.get_by_id(id)
