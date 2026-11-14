square = lambda n: n * n
add = lambda a, b: a + b
print(square(6), add(2, 3))

nums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda n: n * 2, nums)))
print(list(filter(lambda n: n % 2 == 0, nums)))

pairs = [(1, "z"), (2, "a"), (3, "m")]
print(sorted(pairs, key=lambda p: p[1]))

words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
print(max(words, key=lambda w: len(w)))

users = [{"n": "a", "age": 30}, {"n": "b", "age": 20}]
print(sorted(users, key=lambda u: u["age"]))

check = lambda n: "even" if n % 2 == 0 else "odd"
print(check(4), check(7))

from functools import reduce
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]))
