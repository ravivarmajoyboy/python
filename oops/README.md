# Python Concepts

## strings.py

Strings can be sliced, searched and changed with built in methods. Slicing with [::-1] reverses a string, which is how the palindrome check in the file works.

```python
t = "python"
print(t[0], t[-1], t[1:4], t[::-1])
print(f"{3.14159:.2f}")
print("racecar" == "racecar"[::-1])
```

## list.py

Lists keep things in order and you can change them any time. The file shows adding, inserting, removing, sorting, slicing and list comprehensions.

```python
nums.append(7)
nums.insert(0, 10)
nums.remove(2)
print([n * 2 for n in nums if n > 5])
```

## tuples.py

A tuple is like a list that cannot be changed. Because of that it can be used as a dictionary key. A tuple with one item needs a comma at the end, otherwise Python just sees a plain number. Tuples also make swapping easy.

```python
single = (1,)
a, b = 1, 2
a, b = b, a

def min_max(nums):
    return min(nums), max(nums)
```

## set.py

A set has no duplicates and no order. It is good for removing repeats and for comparing two groups. The file shows union, intersection, difference and what is in one but not both. One thing to remember is that empty curly brackets make a dictionary, so use set for an empty set.

```python
print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
print(set([1, 1, 2, 2, 3]))
```

## dictionaries.py

A dictionary stores keys and values. The file shows safe lookups with a default, updating, looping, merging two dictionaries and counting letters in a word, which is a pattern you will use a lot.

```python
print(user.get("email", "none"))
print({**d1, **d2})

count = {}
for ch in "hello":
    count[ch] = count.get(ch, 0) + 1
```

## lambda.py

A lambda is a tiny function written in one line. It is mostly used as the sorting key or inside map and filter. The file also uses reduce to multiply a list of numbers into one.

```python
print(sorted(words, key=lambda w: len(w)))
print(list(filter(lambda n: n % 2 == 0, nums)))
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
```

## asterisk_operator.py

The star does more than multiply. One star collects extra arguments or spreads a list into a function call. Two stars do the same for keyword arguments and dictionaries. It also grabs the leftovers when unpacking and can join lists or dictionaries. The file has an example of every use.

```python
def f(*args, **kwargs):
    print(args, kwargs)

print(add(*nums))
print(add(**d))
first, *rest = [1, 2, 3, 4]
print([*l1, *l2])
print(list(zip(*matrix)))
```

## decorators.py

A decorator is a function that takes another function and gives back a new one. Putting @timer above a function is just a shorter way of wrapping it. The file starts with a simple wrapper, then a timer that keeps the original function name, then a decorator that takes its own argument, then two decorators stacked on one function.

```python
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def slow(n):
    time.sleep(n)
    return "finished"
```

## generators.py

A function with yield gives back one value at a time instead of building the whole list first. The fibonacci example never ends, but that is fine because a value is only made when you ask for it. At the bottom the file compares the memory used by a list and a generator over ten thousand numbers, and the generator is tiny.

```python
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
print([next(f) for _ in range(10)])
```

## itertools.py

Ready made tools for looping. The file covers permutations, combinations, product, chain, count, cycle, repeat, groupby, accumulate, zip_longest, takewhile and dropwhile. The endless ones like count and cycle need islice to cut them off.

```python
print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.accumulate([1, 2, 3, 4])))
```

## exceptions.py

Shows try, except, else and finally together in one function. The else part runs only when nothing went wrong and finally runs every time. Run it and watch the order things print in. The file also shows catching more than one error, making your own error class and raising a different error from inside an except block.

```python
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("cant divide by zero")
    else:
        print("no error")
        return result
    finally:
        print("done")
```

## logging.py

Logging is like print but with levels, timestamps and the option to write to a file. The levels from low to high are debug, info, warning, error and critical. The file sends everything to the console but only warnings and above to app.log. Using logging.exception inside an except block saves the full error trace.

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.WARNING)
```

## json.py

Turns Python data into text and back again. dumps and loads work with strings, dump and load work with files. Python True and None become true and null in JSON. Bad input raises a JSONDecodeError and the file shows how to catch it.

```python
text = json.dumps(data)
back = json.loads(text)

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)
```

## random_numbers.py

Covers random numbers, random choices, samples, shuffling and seeding. Seeding with the same number gives the same result every time, and the file proves it. The last lines matter most. The random module is predictable, so never use it for passwords or tokens. Use the secrets module for that.

```python
random.seed(42)
print(random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100))

print(secrets.token_hex(8))
```

## multithreading.py

Threads run inside one process and share memory. The file starts and joins threads, shows a daemon thread that dies with the program, and fixes a broken shared counter with a lock. It also has a queue with worker threads and the ThreadPoolExecutor, which is the easy way to run many small jobs at once.

```python
counter = 0
lock = threading.Lock()

def add():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
```

## multiprocessing.py

Processes are separate programs, each with its own memory, so sharing data needs special tools. The file shows shared values and arrays with a lock, a queue between processes where None means the work is finished, and a Pool for running a function over many inputs. Everything sits under the main check, because without it Windows and macOS keep spawning new processes forever.

```python
counter = Value("i", 0)
lock = Lock()
ps = [Process(target=add, args=(counter, lock)) for _ in range(4)]

with Pool(4) as pool:
    print(pool.map(square, range(10)))
```

## threading_vs_multiprocessing.py

Runs the same work one after another, with threads and with processes, for two kinds of job. For waiting jobs like sleep, threads and processes both finish in about one second instead of four. For heavy maths, only processes get faster. The reason is the GIL, which lets only one thread run Python code at a time. Exact times depend on your computer.

The simple rule is this. If your program is waiting, use threads. If it is calculating, use processes.

```python
timed("io  threads   ", lambda: run_threads(io_task))
timed("io  processes ", lambda: run_procs(io_task))
timed("cpu threads   ", lambda: run_threads(cpu_task))
timed("cpu processes ", lambda: run_procs(cpu_task))
```
