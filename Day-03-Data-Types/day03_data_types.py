# Day 03 - Comments, Variables and Data Types

# 1. Single-line comment
# This line is ignored by Python
print("Comments are useful for documentation")

# 2. Multi-line string / documentation-style text
"""
This is a multi-line string.
It can be used as documentation.
"""
print("Python")

# 3. Variables
age = 22
name = "Harish"
percentage = 95.5
print(age, name, percentage)

# 4. String
language = "Python"
print(language)
print(language[0])

# 5. Integer
x = 100
print(x)
print(type(x))

# 6. Float
price = 199.99
print(price)
print(type(price))

# 7. Complex
z = 4 + 5j
print(z)
print(z.real)
print(z.imag)

# 8. List - mutable and ordered
numbers = [10, 20, 30, 40]
print(numbers)
print(numbers[0])
numbers[0] = 100
print(numbers)

# 9. Tuple - immutable and ordered
colors = ("red", "green", "blue")
print(colors)
print(colors[1])

# One-element tuple requires a comma
single = (10,)
print(single)
print(type(single))

# 10. Range
r = range(5)
print(r)
print(list(r))

# 11. Boolean
status = True
print(status)
print(type(status))

# 12. None
result = None
print(result)
print(type(result))
