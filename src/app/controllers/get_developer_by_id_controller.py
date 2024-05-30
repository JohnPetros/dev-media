from database import developers_repository


class GetDeveloperByIdController:
    def execute(self, id: str):
        developer = developers_repository.get_by_id(id)
        print("developer", developer, flush=True)
        return developer
