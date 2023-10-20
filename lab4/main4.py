from Article import *
from Comment import *
from Topic import Topic

Articl = Article(input("Name "), int(input("Length ")))

[print("") for i in Articl.addcomments(5)]
Articl.addcomments(4)

print(str(Articl))
Articl.showcomments()

Articl.SaveFile()
Articlee = Article()
Articlee.ReadFile()
print(str(Articlee))
Articlee.showcomments()

