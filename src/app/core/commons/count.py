from .common import Common


class Count(Common):
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise Exception("Count value must be a string")

        self.value = value

    def format(self):
        if self.value.isnumeric() and int(self.value) > 1000:
            self.value = f"{(int(self.value) / 1000):.1f}K"
            return self

        self.value = self.value
        return self
