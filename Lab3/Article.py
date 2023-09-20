class Article(object):
    theme = ""
    length = 0
    comments = []

    def __init__(self, theme: str = "Undefined", length: int = 0):
        self.theme = theme
        self.length = length

    def __str__(self) -> str:
        return f"Publication about {self.theme} with {self.length} length"

    def __eq__(self, other: "Other Article obj") -> bool:
        return (self.theme == other.theme) and (self.length == other.length)

    def addcomment(self,comment: "Comment obj"):
        self.comments.append(comment)

    def showcomments(self):
        for comm in self.comments:
            print(str(comm))