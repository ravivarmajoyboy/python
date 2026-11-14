class A:
    def __init__(self):
        print("init called")

a = A()


class B:
    def __init__(self, x, y):
        self.x = x
        self.y = y

b = B(1, 2)
print(b.x, b.y)
print(b.__dict__)


class C:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

c = C(1, 2, 3, a=4, b=5)
print(c.args, c.kwargs)


class Parent:
    def __init__(self, name):
        self.name = name
        print("parent init")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print("child init")

ch = Child("law", 21)
print(ch.name, ch.age)


class NoInitChild(Parent):
    pass

n = NoInitChild("inherited")
print(n.name)


class Manual:
    def __init__(self, v):
        self.v = v

m = Manual(1)
m.__init__(99)
print(m.v)


class Wrong:
    def __init__(self):
        self.ok = True

print(Wrong().ok)
try:
    class Bad:
        def __init__(self):
            return 5
    Bad()
except TypeError as e:
    print(e)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

print(Point().x, Point(5).x, Point(5, 6).y)
