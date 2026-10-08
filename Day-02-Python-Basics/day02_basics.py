# Day 02 - Python Program, Execution, Tokens and Variables

# 1. Python program
print("Hello World")

# 2. Interactive-mode style examples
print(10 + 20)
name = "Rishitha"
print(name)

# 3. Tokens
# Keywords -> if, else, for, while, class, def
# Identifier -> student_name
# Literal -> 100, 3.14, "Python", True
# Operator -> +, -, *, /
# Delimiters -> (), [], {}, :, ,

student_name = "Rishitha"
marks = 90
total = marks + 10
print(student_name)
print(total)

# 4. Multiple assignment
a, b, c = 10, 20, 30
print(a, b, c)

# 5. Same value to multiple variables
x = y = z = 100
print(x, y, z)

# 6. Reassignment
score = 50
print(score)
score = 80
print(score)

# 7. Swapping
first = 10
second = 20
first, second = second, first
print(first, second)

# 8. Delete a variable
temp = 100
print(temp)
del temp

# Uncommenting the next line will cause NameError
# print(temp)

# 9. Collections introduced through variables
numbers = [10, 20, 30]
student = {"name": "Rishitha", "marks": 90}
unique_numbers = {10, 20, 20, 30}

print(numbers)
print(student)
print(unique_numbers)
