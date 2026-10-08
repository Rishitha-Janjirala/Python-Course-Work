# Day 06 Practice

# Practice 1: Take two numbers and calculate basic operations
a, b = map(int, input("Enter two numbers: ").split())

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

# Practice 2: Read a list of marks
marks = list(map(int, input("Enter marks: ").split()))
total = sum(marks)
average = total / len(marks)

print(f"Total: {total}")
print(f"Average: {average:.2f}")

# Practice 3: Simple formatted profile
name = input("Enter name: ")
age = int(input("Enter age: "))
city = input("Enter city: ")

print("\n--- PROFILE ---")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"City : {city}")
