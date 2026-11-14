import random

print(random.random())
print(random.randint(1, 10))
print(random.uniform(1.5, 5.5))
print(random.randrange(0, 100, 5))

items = ["a", "b", "c", "d"]
print(random.choice(items))
print(random.choices(items, k=3))
print(random.sample(items, 2))

random.shuffle(items)
print(items)

random.seed(42)
print(random.randint(1, 100))
random.seed(42)
print(random.randint(1, 100))

print(random.gauss(0, 1))

password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz0123456789", k=8))
print(password)

import secrets
print(secrets.token_hex(8))
print(secrets.randbelow(100))
