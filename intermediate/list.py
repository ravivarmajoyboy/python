nums = [5, 2, 8, 1, 9]
nums.append(7)
nums.insert(0, 10)
nums.remove(2)
print(nums)

nums.sort()
print(nums)
print(nums[::-1])
print(nums[1:4])
print(nums.pop())
print(len(nums), max(nums), min(nums), sum(nums))

print([n * 2 for n in nums if n > 5])

a = [1, 2]
b = [3, 4]
print(a + b)
print(a * 3)
print(5 in nums)

for i, n in enumerate(nums):
    print(i, n)

matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
