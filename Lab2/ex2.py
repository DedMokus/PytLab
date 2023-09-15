import ipaddress


def ipbyte(ip, mask):
    ipint = tuple(int(n) for n in ip.split('.'))
    maskint = tuple(int(n) for n in mask.split('.'))
    ipsolve = [int(n) for n in range(4)]
    for i in range(4):
        ipsolve[i] = ipint[i] & maskint[i]
    stri = [str(ipsolve[0]), ".", str(ipsolve[1]), '.', str(ipsolve[2]), '.', str(ipsolve[3])]
    return "".join(stri)


mask = input("Input mask")

# print(ipbyte("192.168.1.2",mask))

ipfile = open("ip.log", "r")
ipsolvefile = open("ip_solve.log", "w")

for i in range(1000):
    ip = ipfile.readline().rstrip('\n')
    ips = ipbyte(ip, mask)
    ipsolvefile.write(ips + "\n")

ipfile.close()
ipsolvefile.close()
