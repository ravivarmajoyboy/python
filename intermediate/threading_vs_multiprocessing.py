import time
import threading
import multiprocessing

def cpu_task(n=3_000_000):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_task():
    time.sleep(1)

def timed(label, func):
    start = time.time()
    func()
    print(f"{label}: {time.time() - start:.2f}s")

def run_threads(target, count=4):
    ts = [threading.Thread(target=target) for _ in range(count)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()

def run_procs(target, count=4):
    ps = [multiprocessing.Process(target=target) for _ in range(count)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()

if __name__ == "__main__":
    print("cpus:", multiprocessing.cpu_count())

    timed("io  sequential", lambda: [io_task() for _ in range(4)])
    timed("io  threads   ", lambda: run_threads(io_task))
    timed("io  processes ", lambda: run_procs(io_task))

    timed("cpu sequential", lambda: [cpu_task() for _ in range(4)])
    timed("cpu threads   ", lambda: run_threads(cpu_task))
    timed("cpu processes ", lambda: run_procs(cpu_task))
