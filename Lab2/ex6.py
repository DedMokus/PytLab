# -*- coding: utf-8 -*-
import os

letters = {}
cyrillic = [chr(i) for i in range(ord("а"),ord("я")+1)]
with open("article_rus.txt",mode="r") as file:
    filecontent = file.readlines()

for line in filecontent:
    line.lower()
    for letter in line:
        if letter in cyrillic:
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1

allletters = sum(letters.values())
for let in letters:
    letters[let] = round(letters[let]/allletters,3)

letters = dict(sorted(letters.items(),key = lambda x:x[1],reverse=True))

print(letters)

with open("article_rus_solve.txt","w") as file:
    for let in letters:
        file.write(f"{let}:{letters[let]}\n")