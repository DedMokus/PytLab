import os
import random
import string

if not(os.path.exists("example")):
    os.mkdir("example")
rand = string.ascii_lowercase + string.digits

for i in range(1000):
    filename =  ''.join(random.choice(rand) for j in range(15))
    file = open("example/"+filename,"w")
    file.close()