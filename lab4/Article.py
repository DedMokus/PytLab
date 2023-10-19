import pickle
import random
import string

from lab4.Comment import Comment


class Article:

    def __init__(self, theme: str = "Undefined", length: int = 0):
        try:
            if length < 0:
                raise ValueError
        except ValueError:
            raise ValueError("Incorrect value")

        try:
            self.theme = theme
            self.length = int(length)
            self.comments = []
        except TypeError:
            raise TypeError("Str in int")
    def __str__(self) -> str:
        return f"Publication about {self.theme} with {self.length} length"

    def __eq__(self, other: "Other Article obj") -> bool:
        return (self.theme == other.theme) and (self.length == other.length)

    def SaveFile(self):
        print("Load data to file")
        data = [("theme",self.theme), ("length", self.length), ("comments", self.comments)]
        try:
            with open("prod_file.pkl", "wb") as f_o:
                pickle.dump(data, f_o)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

    def ReadFile(self):
        try:
            with open("prod_file.pkl", "rb") as f_o:
                data = pickle.load(f_o)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")

        dct = dict()
        try:
            for inf in data:
                dct[inf[0]] = inf[1]

            self.theme = dct['theme']
            self.length = dct['length']
            self.comments = dct['comments']
        except ValueError:
            raise ValueError("Value error on DB")

        except KeyError:
            raise KeyError("Missing entry in DB")


    def addcomments(self, count):
        letters = string.ascii_lowercase
        i=0
        for i in range(count):
            name = ''.join(random.choice(letters) for i in range(10))
            comment = ''.join(random.choice(letters) for i in range(10))
            comm = Comment(name, comment)
            self.addcomment(comm)
            yield name

    def addcomment(self, comment: "Comment obj"):
        self.comments.append(comment)

    def showcomments(self):
        for comm in self.comments:
            print(str(comm))
