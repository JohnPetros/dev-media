class Count:
    def __init__(self, value: str):
        if not isinstance(value, str):
            raise Exception("Count value must be a string")

        self.value = value

    def format(self):
        if not self.value.isnumeric():
            return self

        if int(self.value) >= 1_000_000:
            self.value = f"{(int(self.value) / 1_000_000):.1f}M"
            return self

        if int(self.value) >= 1_000:
            self.value = f"{(int(self.value) / 1_000):.1f}K"
            return self

        return self

    def get_value(self):
        return self.value
