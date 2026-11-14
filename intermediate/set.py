a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

a.add(10)
a.remove(1)
a.discard(99)
print(a)

print(set([1, 1, 2, 2, 3]))
print(list(set([3, 1, 3, 2])))

print({1, 2} <= {1, 2, 3})
print({1, 2}.isdisjoint({3, 4}))

print({n % 3 for n in range(10)})

empty = set()
print(type(empty))

print(2 in a)
