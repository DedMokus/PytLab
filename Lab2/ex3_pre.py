import csv
import random

names = ["Петров","Арефьев","Лебедев","Костин","Красавин","Трусов","Дегтев","Коротов","Криницкий","Павлов","Будин"]
headings = ["Спортсмен","Кол-во побед","Доп. баллы"]

data = [[names[x] for x in range(len(names))],
        [random.randint(1,10) for x in range(len(names))],
        [random.randint(10,1000) for x in range(len(names))]]

for i in range(3):
    data[i].insert(0,headings[i])

tr_data = [[0 for j in range(len(data))] for i in range(len(data[0]))]


for i in range(len(data)):
    for j in range(len(data[0])):
        tr_data[j][i] = data[i][j]

with open("players.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(tr_data)


