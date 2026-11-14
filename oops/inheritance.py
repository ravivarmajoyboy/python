class Item:
    pay_rate = 0.8

    def __init__(self, name, price, qty=1):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.price * self.qty

    def apply_discount(self):
        self.price = self.price * self.pay_rate


class Phone(Item):
    def __init__(self, name, price, qty=1, broken=0):
        super().__init__(name, price, qty)
        self.broken = broken

    def working(self):
        return self.qty - self.broken

p = Phone("iphone", 500, 5, 1)
print(p.total())
print(p.working())
p.apply_discount()
print(p.price)
print(Phone.pay_rate)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

class Dog(Animal):
    def speak(self):
        print(self.name, "woof")

class Cat(Animal):
    def speak(self):
        print(self.name, "meow")

for a in [Dog("rex"), Cat("tom"), Animal("x")]:
    a.speak()


class A:
    def hi(self):
        print("A")

class B(A):
    pass

class C(B):
    pass

C().hi()
print(C.__mro__)
print(issubclass(C, A), isinstance(C(), B))


class Flyer:
    def fly(self):
        print("flying")

class Swimmer:
    def swim(self):
        print("swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()
print([c.__name__ for c in Duck.__mro__])
