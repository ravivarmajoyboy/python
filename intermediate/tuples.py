point = (3, 4)
print(point[0], point[1])

x, y = point
print(x, y)

print(point + (5, 6))
print(point * 2)
print(len(point))
print(point.count(3), point.index(4))

single = (1,)
print(type(single))

a, *rest = (1, 2, 3, 4)
print(a, rest)

a, b = 1, 2
a, b = b, a
print(a, b)

def min_max(nums):
    return min(nums), max(nums)

print(min_max([4, 1, 9]))

d = {(1, 2): "key is a tuple"}
print(d[(1, 2)])
