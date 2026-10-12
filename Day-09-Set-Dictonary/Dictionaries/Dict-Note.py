# 1.Dictionaries

# A dictionary stores data in key-value pairs.

# Properties:
# Maintains insertion order
# Mutable
# Values are accessed using keys
# Keys must be unique
# Duplicate values are allowed
# Supports different data types
# Can store nested data structures

# Dictionary Operations
# Accessing values using keys
# Updating existing values
# Adding new key-value pairs
# Removing items
# Checking key membership


# Built-in Functions
# len(), max(), min(), sorted(), dict(), any(), all()

# Dictionary Methods:
# Accessing: get(), keys(), values(), items()
# Adding and updating: update(), setdefault()
# Removing: pop(), popitem(), clear()

# Copying: copy()
# Creating: fromkeys()

# Example

student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python"
}

print(student["name"])

student["age"] = 23
student["city"] = "Hyderabad"

print(student)
print(student.keys())
print(student.values())
print(student.items())

# 2. Nested Dictionary

# A dictionary inside another dictionary is called a nested dictionary.

students = {
    "s1": {"name": "Ravi", "age": 22},
    "s2": {"name": "Teja", "age": 21}
}

print(students["s1"]["name"])