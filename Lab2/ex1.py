import os
import re
from random import *

def checkIP(ip):
    ipv4 = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(
25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'''
    return re.search(ipv4,ip)

def setIP():
    ip = ".".join(map(str,(randint(0,255) for _ in range(4))))
    return ip

FILENAME = "ip.log"
with open(FILENAME,"w") as file:
    for i in range(1000):
        file.write(setIP()+"\n")
