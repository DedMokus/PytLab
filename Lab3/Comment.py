class Comment(object):
    name = ""
    text = ""

    def __init__(self, name: str = "Unknown", text: str = "Undefined"):
        self.text = text
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}: {self.text}"
