class ValueNotProvidedError(Exception):
    def __init__(self, value_name: str):
        self.message = f"{value_name} value is not provided"

        super().__init__(self.message)
