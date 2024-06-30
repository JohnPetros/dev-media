class EntityNotFoundError(Exception):
    def __init__(self, entity_name: str) -> None:
        self.message = f"{entity_name} entity is not found"

        super().__init__(self.message)
