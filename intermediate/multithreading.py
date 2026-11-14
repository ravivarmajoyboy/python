import time
import threading
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

def work(name, secs):
    print(name, "start")
    time.sleep(secs)
    print(name, "end")

t1 = threading.Thread(target=work, args=("t1", 1))
t2 = threading.Thread(target=work, args=("t2", 1))
t1.start()
t2.start()
t1.join()
t2.join()
print("both done")

d = threading.Thread(target=work, args=("daemon", 5), daemon=True)
d.start()
print(d.is_alive())


counter = 0
lock = threading.Lock()

def add():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

ts = [threading.Thread(target=add) for _ in range(4)]
for t in ts:
    t.start()
for t in ts:
    t.join()
print(counter)


q = Queue()

def worker():
    while True:
        item = q.get()
        print("processing", item)
        q.task_done()

for _ in range(2):
    threading.Thread(target=worker, daemon=True).start()
for i in range(5):
    q.put(i)
q.join()
print("queue done")


def square(n):
    time.sleep(0.2)
    return n * n

with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(square, range(8)))
print(results)

with ThreadPoolExecutor(max_workers=2) as ex:
    f = ex.submit(square, 9)
    print(f.result())
