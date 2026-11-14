import itertools

print(list(itertools.permutations([1, 2, 3], 2)))
print(list(itertools.combinations([1, 2, 3, 4], 2)))
print(list(itertools.product("ab", repeat=2)))
print(list(itertools.chain([1, 2], [3, 4])))

print(list(itertools.islice(itertools.count(10), 5)))
print(list(itertools.islice(itertools.cycle("ab"), 5)))
print(list(itertools.repeat("x", 3)))

for key, group in itertools.groupby("aaabbc"):
    print(key, list(group))

print(list(itertools.accumulate([1, 2, 3, 4])))
print(list(itertools.zip_longest([1, 2, 3], ["a"], fillvalue="-")))
print(list(itertools.takewhile(lambda n: n < 5, [1, 3, 5, 2])))
print(list(itertools.dropwhile(lambda n: n < 5, [1, 3, 5, 2])))
