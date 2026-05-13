# NameError: name 'result' is not defined
print(result)

# ZeroDivisionError: division by zero
print(10 / 0)

# TypeError: unsupported operand type(s) for /: 'int' and 'str'
print(10 / "0")

# ValueError: invalid literal for int() with base 10: 'ten'
print(int("ten"))

# IndexError: list index out of range
print([1, 2, 3][3])

# KeyError: 'age'
print({"name": "John", "age": 30}["age"])

# AttributeError: 'str' object has no attribute 'append'
print("Hello".append("World"))

# ImportError: cannot import name 'requests' from 'requests' (unknown location)
import requests

# FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
with open("data.csv", "r") as file:
  print(file.read())

