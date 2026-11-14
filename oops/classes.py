class Empty:
    pass

e = Empty()
print(e, type(e))


class Dog:
    species = "canine"

    def bark(self):
        print("woof")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

d1 = Dog()
d2 = Dog()
d1.bark()
d1.set_name("rex")
d2.set_name("max")
print(d1.get_name(), d2.get_name())
print(d1.species, Dog.species)

d1.age = 3
print(d1.age)
print(hasattr(d1, "age"), hasattr(d2, "age"))
print(d1.__dict__)

print(isinstance(d1, Dog))
print(d1 == d2)
print(id(d1) == id(d2))


class Animal:
    def eat(self):
        print("eating")

class Cat(Animal):
    def meow(self):
        print("meow")

c = Cat()
c.eat()
c.meow()
print(issubclass(Cat, Animal))


class Calc:
    def add(self, a, b):
        return a + b

    def mul(self, a, b):
        return a * b

print(Calc().add(2, 3), Calc().mul(2, 3))
