import os

files = os.listdir("example/")

name = input("Import substring\n")

i = 0
for file in files:
    if name in file:
        i+=1

print(f"Substr {name} is in {i} file names")