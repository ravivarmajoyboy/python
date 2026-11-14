s = "  Hello, World  "
print(s.strip())
print(s.lower())
print(s.upper())
print(s.strip().split(","))
print("-".join(["a", "b", "c"]))
print(s.replace("World", "Python"))

t = "python"
print(t[0], t[-1], t[1:4], t[::-1])
print(len(t))

print(t.startswith("py"), t.endswith("on"))
print(t.find("th"), t.count("y"))
print(t.capitalize(), t.title())

name = "law"
age = 21
print(f"hi {name}, age {age}")
print("hi {} age {}".format(name, age))
print(f"{3.14159:.2f}")

print("abc".isalpha(), "123".isdigit())
print("a b c".split())
print("racecar" == "racecar"[::-1])
print(ord("a"), chr(98))
print("ha" * 3)
