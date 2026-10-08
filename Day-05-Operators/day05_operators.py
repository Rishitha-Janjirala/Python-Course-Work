# Day 05 - Python Operators

# 1. Arithmetic operators
a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor division
print(a % b)   # Modulus
print(a ** b)  # Exponent

# 2. Assignment operators
x = 10
x += 5
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
x //= 2
print(x)
x %= 3
print(x)

# 3. Comparison operators
p = 100
q = 50
print(p > q)
print(p < q)
print(p == q)
print(p != q)
print(p >= q)
print(p <= q)

# 4. Logical operators
marks = 85
age = 21
print(marks >= 60 and age >= 18)
print(marks >= 90 or age >= 18)
print(not (marks >= 90))

# 5. Bitwise operators
m = 10       # 1010
n = 15       # 1111
print(m & n)   # AND
print(m | n)   # OR
print(m ^ n)   # XOR
print(~m)      # NOT
print(m << 2)  # Left shift
print(m >> 2)  # Right shift

# 6. Membership operators
ids = [101, 102, 103]
print(101 in ids)
print(105 in ids)
print(105 not in ids)

# 7. Identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # Same object
print(a is c)      # Different objects
print(a == c)      # Same value

# None check
result = None
print(result is None)

# 8. Conditional / ternary operator
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)
