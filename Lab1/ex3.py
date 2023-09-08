import re


def checkDate(date):
    datere = '\d\d\.\d\d\.\d{4}'
    return re.search(datere,date)


def checkIP(ip):
    ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    return re.search(ipv4,ip)

def checkStr(date,ip):
    if checkDate(date) and checkIP(ip):
        return True
    else:
        return False


def uniqAppend(mass,app):
    name = app[0]
    date = app[1]
    ip = app[2]
    wtf = next((subl for subl in mass if name in subl),[])
    if wtf == []:
        mass.append([name,{ip}])
    else:
        wtf[1].add(ip)


#admin 12.12.2011 1.1.1.1
data = []
users = []
ips = {}
n = int(input("Введите кол-во строк"))

for i in range(n):
    buf = input()
    data.append([])
    [data[i].append(k) for k in buf.split(' ')]
    #print("Data",data[i])
    preq = False
    #print("all",checkStr(data[i][1], data[i][2]))
    while not(preq):
        preq = checkStr(data[i][1],data[i][2])
        if not(preq):
            print("Format error!")
    uniqAppend(users,data[i])

print(users)

for i in users:
    ips[i[0]] = (len(i[1]))
print(ips)

print(max(ips,key=ips.get))
