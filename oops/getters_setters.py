class Item:
    def __init__(self, name, price):
        self.__name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("name too long")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price cant be negative")
        self.__price = value

i = Item("phone", 100)
print(i.name, i.price)

i.name = "laptop"
i.price = 200
print(i.name, i.price)

try:
    i.name = "a very long name here"
except Exception as e:
    print(e)

try:
    i.price = -5
except ValueError as e:
    print(e)

try:
    print(i.__name)
except AttributeError as e:
    print(e)
print(i._Item__name)


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.14159 * self.r ** 2

    @property
    def diameter(self):
        return self.r * 2

    @diameter.setter
    def diameter(self, d):
        self.r = d / 2

c = Circle(5)
print(c.area, c.diameter)
c.diameter = 20
print(c.r)


class ReadOnly:
    def __init__(self, v):
        self.__v = v

    @property
    def v(self):
        return self.__v

r = ReadOnly(1)
print(r.v)
try:
    r.v = 2
except AttributeError as e:
    print(e)


class Old:
    def __init__(self):
        self._x = 0

    def get_x(self):
        return self._x

    def set_x(self, v):
        self._x = v

    x = property(get_x, set_x)

o = Old()
o.x = 7
print(o.x)
