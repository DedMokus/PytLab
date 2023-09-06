
mass = []
massb = []

A = input()

for i in A.split(" "):
    mass.append(i)

for n in mass:
    by = bin(int(n))[2:]
    num = by.count("1")
    massb.append([num,int(n)])

massb.sort()
mass = []

for sublist in massb:
    mass.append(sublist[1])

print(mass)