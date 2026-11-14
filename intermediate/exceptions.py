def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("cant divide by zero")
    except TypeError as e:
        print("type error:", e)
    else:
        print("no error")
        return result
    finally:
        print("done")

print(divide(10, 2))
divide(10, 0)
divide(10, "a")

try:
    int("abc")
except ValueError as e:
    print("value error:", e)

try:
    [1, 2][5]
except (IndexError, KeyError) as e:
    print("caught:", e)

try:
    open("nofile.txt")
except FileNotFoundError:
    print("file not found")

class MyError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise MyError("age cant be negative")
    return age

try:
    check_age(-1)
except MyError as e:
    print(e)

try:
    try:
        1 / 0
    except ZeroDivisionError:
        raise ValueError("re-raised as value error")
except ValueError as e:
    print(e)
