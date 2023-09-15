import csv
import operator

data = []
with open("players.csv","r",newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

print(data)

data = sorted(data, key = operator.itemgetter(1,2),reverse=True)

print(data)

with open("results.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)