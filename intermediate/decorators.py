import time
from functools import wraps

def shout(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@shout
def hello():
    print("hello")

hello()

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

print(slow(0.2))

def repeat(times):
    def deco(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return deco

@repeat(3)
def greet(name):
    print("hi", name)

greet("law")

def log_calls(func):
    def wrapper(*args, **kwargs):
        print("calling", func.__name__, args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_calls
@timer
def add(a, b):
    return a + b

print(add(2, 3))
