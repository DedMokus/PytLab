import random
import time
from threading import Thread, current_thread
from queue import Queue

queue = Queue(100)


def x(que):
    for j in range(10):
        for i in range(10):
            val = random.randint(1,10)
            time.sleep(val/10)
            que.put(val)
        que.put(None)
    print("X - done")


def f(que):
    while True:
        val = que.get()
        if val is None:
            print(current_thread().name,"stop")
            break
        print(current_thread().name, f"val-{val}")



Thread(target=x,args=(queue,)).start()
for i in range(1, 11):
    Thread(target=f, args=(queue,), name=f"name thread-{i}").start()
