# Day 06 - Input Formatting and Output Formatting

# ---------------- INPUT ----------------

# 1. String input
name = input("Enter your name: ")
print(name)

# 2. Integer input
age = int(input("Enter your age: "))
print(age)

# 3. Float input
price = float(input("Enter price: "))
print(price)

# 4. Space-separated list of strings
names = input("Enter names: ").split()
print(names)

# 5. Comma-separated input
tags = input("Enter tags: ").split(",")
print(tags)

# 6. List of integers
marks = list(map(int, input("Enter marks: ").split()))
print(marks)

# 7. List of floats
weights = list(map(float, input("Enter weights: ").split()))
print(weights)

# 8. Tuple input
dimensions = tuple(map(int, input("Enter length width height: ").split()))
print(dimensions)

# 9. Set input
selected_ids = set(map(int, input("Enter IDs: ").split()))
print(selected_ids)

# 10. Multiple inputs using unpacking
username, password = input("Enter username and password: ").split()
print("Username:", username)
print("Password:", password)

# ---------------- OUTPUT ----------------

# Basic print
print("Hello, World!")

# Multiple items
name = "Alice"
age = 25
print("Name:", name, "Age:", age)

# sep
print("2026", "10", "08", sep="-")

# end
print("Hello", end=" ")
print("World!")

# Escape sequences
print("Line 1\nLine 2")
print("Name:\tAlice")

# Old % formatting
score = 88.756
print("Score: %.2f" % score)

# str.format()
print("Name: {} | Age: {} | Score: {:.2f}".format(name, age, score))

# f-string - recommended
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")

# Alignment and width
print(f"{'Name':<10}{'Score':>10}")
print(f"{name:<10}{score:>10.2f}")
