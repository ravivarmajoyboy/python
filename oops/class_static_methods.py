class Item:
    pay_rate = 0.8
    all_items = []

    def __init__(self, name, price, qty=1):
        self.name = name
        self.price = price
        self.qty = qty
        Item.all_items.append(self)

    def total(self):
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def from_csv(cls, line):
        name, price, qty = line.split(",")
        return cls(name, float(price), int(qty))

    @classmethod
    def set_rate(cls, rate):
        cls.pay_rate = rate

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        return isinstance(num, int)

i1 = Item("phone", 100, 2)
print(i1.total())

i2 = Item.from_csv("laptop,1000,3")
print(i2.name, i2.price, i2.qty)

Item.set_rate(0.5)
i1.apply_discount()
print(i1.price)

print(Item.is_integer(5))
print(Item.is_integer(5.0))
print(Item.is_integer(5.5))
print(Item.is_integer("5"))

print(len(Item.all_items))
print([i.name for i in Item.all_items])


class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def from_string(cls, s):
        d, m, y = map(int, s.split("-"))
        return cls(d, m, y)

    @staticmethod
    def is_leap(y):
        return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

dt = Date.from_string("14-11-2026")
print(dt.d, dt.m, dt.y)
print(Date.is_leap(2024), Date.is_leap(2026))
