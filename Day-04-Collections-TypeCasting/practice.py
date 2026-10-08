# Day 04 Practice

# 1. Remove duplicate values
numbers = [10, 20, 10, 30, 20, 40]
unique = set(numbers)
print(unique)

# 2. Student dictionary
student = {
    "name": "Rishitha",
    "course": "Python",
    "score": 88
}
print(student["name"])
print(student.get("course"))

# 3. Convert string to list
text = "PYTHON"
print(list(text))

# 4. Convert list to tuple
items = [10, 20, 30]
print(tuple(items))

# 5. Check truth values
print(bool(""))
print(bool("Python"))
print(bool(0))
print(bool(10))
print(bool([]))
print(bool([1, 2, 3]))

# 6. Convert marks
marks = "90"
marks = int(marks)
print(marks + 10)
