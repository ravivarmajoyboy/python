from abc import ABC, abstractmethod

# ---------- encapsulation ----------
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amt):
        if amt > 0:
            self.__balance += amt

    def withdraw(self, amt):
        if 0 < amt <= self.__balance:
            self.__balance -= amt

    def get_balance(self):
        return self.__balance

a = Account("law", 100)
a.deposit(50)
a.withdraw(30)
print(a.get_balance())


# ---------- abstraction ----------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.s ** 2

    def perimeter(self):
        return 4 * self.s

print(Square(4).area(), Square(4).perimeter())
try:
    Shape()
except TypeError as e:
    print(e)


# ---------- inheritance ----------
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def role(self):
        return "employee"

class Manager(Employee):
    def __init__(self, name, salary, team):
        super().__init__(name, salary)
        self.team = team

    def role(self):
        return "manager"

m = Manager("law", 1000, ["a", "b"])
print(m.name, m.role(), m.team)


# ---------- polymorphism ----------
class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.r

shapes = [Square(2), Circle(3), Square(5)]
for s in shapes:
    print(type(s).__name__, s.area())

print(len("abc"), len([1, 2]), len({1: 2}))
print(1 + 2, "a" + "b", [1] + [2])


class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

print(Vec(1, 2) + Vec(3, 4))
