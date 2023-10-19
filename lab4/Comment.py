class Comment:
    name = ""
    text = ""

    def __init__(self, name: str = "Unknown", text: str = "Undefined"):
        try:
            if (text.__eq__("") or name.__eq__("")):
                raise ValueError
        except ValueError:
            raise ValueError("Incorrect Value")

        self.text = text
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}: {self.text}"
