def checkDate(date):
    spl = [int(x) for x in date.split(".")]
    #print("spl_date",spl)
    length = len(spl)
    #print("in_date",length)
    if length != 3:
        #print("False in length")
        return False
    elif (0 > spl[0]) or (spl[0] > 32):
        #print("False in day")
        return False
    elif (0 > spl[1]) or (spl[1] > 13):
        #print("False in month")
        return False
    elif (2000 > spl[2]) or (spl[2] > 2100):
        #print("False in year")
        return False
    else:
        return True


def checkIP(ip):
    spl = [int(x) for x in ip.split(".")]
    #print("spl_ip",spl)
    length = len(spl)
    #print("in_ip",length)
    if length != 4:
        return False
    elif (0 >= spl[0]) or (spl[0] >= 255):
        return False
    elif (0 >= spl[1]) or (spl[1] >= 255):
        return False
    elif (0 >= spl[2]) or (spl[2] >= 255):
        return False
    elif (0 >= spl[3]) or (spl[3] >= 255):
        return False
    else:
        return True


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
