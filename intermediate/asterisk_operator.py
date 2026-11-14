print(3 * 4)
print(2 ** 5)
print("ab" * 3)
print([0] * 4)

def f(*args, **kwargs):
    print(args, kwargs)

f(1, 2, a=3)

def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add(*nums))
d = {"a": 1, "b": 2, "c": 3}
print(add(**d))

def kw_only(a, *, b):
    return a + b

print(kw_only(1, b=2))

first, *rest = [1, 2, 3, 4]
print(first, rest)
*init, last = [1, 2, 3, 4]
print(init, last)
a, *mid, z = [1, 2, 3, 4, 5]
print(a, mid, z)

l1 = [1, 2]
l2 = [3, 4]
print([*l1, *l2])
print((*l1, *l2))
print({*l1, *l2})

d1 = {"a": 1}
d2 = {"b": 2}
print({**d1, **d2})

print(*[1, 2, 3])
print(*"abc", sep="-")

matrix = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*matrix)))
