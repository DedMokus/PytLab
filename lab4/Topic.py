from Article import Article


class Topic(Article):
    def __init__(self, theme: str = "Undefined", length: int = 0, notes: str = "Undefined"):
        try:
            if length < 0:
                raise ValueError
        except ValueError:
            raise ValueError("Incorrect value")

        self.theme = theme
        self.length = length
        self.comments = []
        self.notes = notes

    def __str__(self) -> str:
        return f"Topic about {self.theme} with {self.length} length. Has note: {self.notes}"
