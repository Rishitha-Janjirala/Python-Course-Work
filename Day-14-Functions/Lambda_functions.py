# Lambda Functions (Anonymous Functions)
# Definition:
# - A lambda function is a function without a name.
# - It is created using the lambda keyword.
# - Used for short and simple operations in a single line.
# - It automatically returns the result without using return.
# Syntax:
# lambda arguments: expression

# Examples:

# 1. No Parameters
# a = lambda: 10print(a())# Output: 10


# 2. One Parameter
# square = lambda x: x*xprint(square(5))# Output: 25


# 3. Multiple Parameters
# add = lambda x, y: x+yprint(add(10, 20))# Output: 30


# 4. Using Lambda with Conditions
# check = lambda x: "Even" if x%2==0 else "Odd"print(check(5))# Output: Odd

# Advantages:
# 1. Short and concise code.
# 2. No need to use def.
# 3. Automatically returns a value.
# 4. Useful with map(), filter() and reduce().


# 1. Adding Two Numbers
add=lambda a,b:a+b
print(add(10,20))

# 2. Square of a Number
sq=lambda a:a*a
print(sq(10))

#3.even or odd
is_even=lambda num:num%2==0
print(is_even(8))

#4.Find Maximum of Two Numbers
maxi=lambda a,b: a if a>b else b
print(maxi(20,40))

#Product of two numbers
prod=lambda a,b:a*b
print(prod(10,3))

#Strings length
length=lambda strs:len(strs)
print(length("Rishitha"))

# Filter Function:
# The filter() function is used to select elements from an iterable based on a condition.
# Only elements that satisfy the condition are returned.

# 1: Even Numbers
nums=[2,3,4,5,6,7,8,9]
res=list(filter(lambda x:x%2==0,nums))
print(res)

#odd numbers
nums=[2,3,4,5,6,7,8,9]
res=list(filter(lambda x:x%2==1,nums))
print(res)

#products above 1000
prices=[2000,3000,4000,2500,500]
res=list(filter(lambda p:p>1000,prices))
print(res)

#long usernames
users=["Rishitha","srikar",'Srinu',"Bhavani"]
res=list(filter(lambda s:len(s)>5,users))
print(res)

# Reduce Function:
# The reduce() function reduces an iterable into a single value. It repeatedly applies a
# function to combine elements.

#1.sum of numbers
from functools import reduce
nums=[1,2,3,4,5,6]
res=reduce(lambda a,b:a+b,nums)
print(res)

#2.prod of numbers
from functools import reduce
nums=[1,2,3,4,5,6]
res=reduce(lambda a,b:a*b,nums)
print(res)

# 3.Largest Number
from functools import reduce
numbers = [10, 25, 8, 40, 15]
result = reduce(lambda a, b: a if a > b else b, numbers)
print(result)


# Map Function:
# The map() function applies a transformation to every element in an iterable.

#1:Square Numbers
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * x, numbers))
print(result)

# 2: Convert Names to Uppercase
names = ["teja", "ravi", "sneha"]
result = list(map(lambda name: name.upper(), names))
print(result)

# 3: Add GST
prices = [1000, 2000, 3000]
result = list(map(lambda x: x + (x * 0.18), prices))
print(result)

# 4: Calculate String Length
words = ["python", "java", "sql"]
result = list(map(lambda word: len(word), words))
print(result)

