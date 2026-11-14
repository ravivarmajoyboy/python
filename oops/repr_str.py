class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

i = Item("phone", 100)
print(i)
print(repr(i))


class Item2:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item2('{self.name}', {self.price})"

i2 = Item2("phone", 100)
print(i2)
print([i2, Item2("laptop", 900)])


class Item3:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item3({self.name!r}, {self.price!r})"

    def __str__(self):
        return f"{self.name} costs {self.price}"

i3 = Item3("phone", 100)
print(i3)
print(str(i3))
print(repr(i3))
print([i3])
print(f"{i3}")
print(eval(repr(i3)).name)
