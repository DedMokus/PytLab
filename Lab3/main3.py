from Article import *
from Comment import *

Articles = []

Articles.append(Article())
Articles.append(Article(input("Name "), int(input("Length "))))

Comment1 = Comment()
Comment2 = Comment(input("Name "), input("Comment "))

print(Articles[0] == Articles[1])

Articles[0].addcomment(Comment1)
Articles[1].addcomment(Comment2)

print(str(Articles[0]))
Articles[0].showcomments()
print(str(Articles[1]))
Articles[1].showcomments()