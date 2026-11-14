user = {"name": "law", "age": 21}
user["role"] = "red team"
user["age"] = 22
print(user)

print(user["name"])
print(user.get("email", "none"))

del user["role"]
print(user.pop("age"))
print(user)

user.update({"city": "x", "lang": "python"})
print(user.keys())
print(user.values())

for k, v in user.items():
    print(k, v)

print("name" in user)

print({n: n ** 2 for n in range(5)})

d1 = {"a": 1}
d2 = {"b": 2}
print({**d1, **d2})

count = {}
for ch in "hello":
    count[ch] = count.get(ch, 0) + 1
print(count)

nested = {"a": {"b": {"c": 1}}}
print(nested["a"]["b"]["c"])
