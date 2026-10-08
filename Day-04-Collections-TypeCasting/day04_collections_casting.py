# Day 04 - Set, Dictionary, Boolean, None and Type Casting

# 1. Set
student_ids = {101, 102, 103, 101}
print(student_ids)
print(type(student_ids))

# Empty set
empty_set = set()
print(empty_set)
print(type(empty_set))

# {} creates an empty dictionary
empty_dict = {}
print(type(empty_dict))

# 2. Dictionary
student = {
    "name": "Rishitha",
    "age": 21,
    "marks": 90,
    "city": "Hyderabad"
}

print(student)
print(student["name"])
print(student["city"])

# get() avoids KeyError and can return a default value
print(student.get("marks"))
print(student.get("phone", "Not Available"))

# 3. Boolean
is_logged_in = True
print(is_logged_in)
print(type(is_logged_in))

# 4. None
payment_status = None
print(payment_status)
print(type(payment_status))

# 5. Implicit type conversion
a = 10
b = 2.5
result = a + b
print(result)
print(type(result))

# 6. Explicit type conversion
x = "100"
print(int(x))

price = 99
print(float(price))

number = 123
print(str(number))

print(bool(1))
print(bool(0))

# Sequence conversions
numbers = [1, 2, 3, 4]
print(tuple(numbers))
print(set(numbers))

name = "Python"
print(list(name))
print(tuple(name))
print(set(name))

# Dictionary conversion from key-value pairs
pairs = [("name", "Rishitha"), ("age", 21)]
print(dict(pairs))

# Common conversion errors:
# int("10.5") -> ValueError
# int("abc") -> ValueError
# list(10) -> TypeError because int is not iterable
