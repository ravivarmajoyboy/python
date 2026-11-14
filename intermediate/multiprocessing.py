import time
from multiprocessing import Process, Value, Array, Lock, Queue, Pool, cpu_count

def square(n):
    return n * n

def add(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

def put_items(q):
    for i in range(3):
        q.put(i)
    q.put(None)

if __name__ == "__main__":
    print(cpu_count())

    p = Process(target=square, args=(5,))
    p.start()
    p.join()
    print("process done", p.exitcode)

    counter = Value("i", 0)
    lock = Lock()
    ps = [Process(target=add, args=(counter, lock)) for _ in range(4)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    print(counter.value)

    arr = Array("d", [1.0, 2.0, 3.0])
    print(list(arr))

    q = Queue()
    p = Process(target=put_items, args=(q,))
    p.start()
    while True:
        item = q.get()
        if item is None:
            break
        print("got", item)
    p.join()

    with Pool(4) as pool:
        print(pool.map(square, range(10)))
        print(pool.apply(square, (7,)))
        res = pool.apply_async(square, (8,))
        print(res.get())
