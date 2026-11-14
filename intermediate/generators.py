def count_up(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for i in count_up(5):
    print(i)

gen = count_up(3)
print(next(gen))
print(next(gen))
print(next(gen))

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fib()
print([next(f) for _ in range(10)])

squares = (n * n for n in range(5))
print(list(squares))
print(sum(n for n in range(1000)))

def read_lines(text):
    for line in text.split("\n"):
        yield line.strip()

for line in read_lines("a\n b \nc"):
    print(line)

def inner():
    yield 1
    yield 2

def outer():
    yield from inner()
    yield 3

print(list(outer()))

import sys
print(sys.getsizeof([n for n in range(10000)]))
print(sys.getsizeof(n for n in range(10000)))
