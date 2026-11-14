class NoConstructor:
    pass

n = NoConstructor()
print(n)


class Basic:
    def __init__(self):
        print("object created")
        self.value = 10

b = Basic()
print(b.value)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("law", 21)
print(p.name, p.age)


class Server:
    def __init__(self, host, port=80, secure=False):
        self.host = host
        self.port = port
        self.secure = secure

s1 = Server("a.com")
s2 = Server("b.com", 443, True)
s3 = Server("c.com", secure=True)
print(s1.port, s2.port, s3.port, s3.secure)


class Temp:
    def __init__(self, celsius):
        if celsius < -273:
            raise ValueError("below absolute zero")
        self.celsius = celsius
        self.fahrenheit = celsius * 9 / 5 + 32

t = Temp(100)
print(t.fahrenheit)
try:
    Temp(-300)
except ValueError as e:
    print(e)


class Box:
    count = 0

    def __init__(self):
        Box.count += 1
        self.id = Box.count

Box()
Box()
b3 = Box()
print(b3.id, Box.count)


class Copyable:
    def __init__(self, items=None):
        self.items = items if items is not None else []

x = Copyable()
y = Copyable()
x.items.append(1)
print(x.items, y.items)
