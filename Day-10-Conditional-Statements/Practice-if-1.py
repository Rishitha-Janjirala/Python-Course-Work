#Basic Level Questions

#1.Take an integer input from the user and print whether it is positive or negative.
n=int(input("enter num: "))
if n>0:
    print(f"num {n} is +ve")
else:
    print(f"num {n} is -ve")


# 2.Take an input number from the user and check whether it is even or odd.
num=int(input("enter num:"))
if num%2==0:
    print("num is even",num)
else:
    print("num is odd",num)


# 3.Ask the user for their age. If the age is 18 or more, print “You are eligible to vote.”
age=int(input("enter your age:"))
if age>=18:
    print('You are eligible age:',age)
else:
    print('You are not eligible age:',age)


# 4.Take marks input from the user and print:
# -->"Pass" if marks >= 35
# -->"Fail" otherwise
marks=int(input("enter marks:"))
if marks>=35:
    print("Pass")
else:
    print("Fail")


# 5.Take two numbers as input and print the greater number.
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
if num1>num2:
    print("num1 is greater num:",num1)
else:
    print("num2 is greater num:",num2)


#6.Check if a given number is a multiple of 5 or not.
num=int(input("enter num:"))
if num%5==0:
    print(f"{num} is multiple of 5")
else:
    print(f"{num} is not multiple of 5")


#7.Take a number input and print whether it is divisible by 3 and 5.
n=int(input())
if n%3==0 and n%5==0:
    print(f"{num} is divisible by both 3 and 5")
else:
    print(f"{num} is not divisible by both 3 and 5")


#8.Take a character input and check if it is a vowel or consonant.
char=input()
if char in "aeiouAEIOU":
    print(f"{char} is vowel")
else:
    print(f"{char} is consonant")


# 9.Ask the user to enter their name. If the name is “admin”, print “Welcome, Admin!”
name=input("enter your name")
if name=="admin":
    print("Welcome,Admin")
    

#10.Take a number input and print “Zero” if it is 0, otherwise print “Non-Zero”
number=int(input("enter value:"))
if number==0:
    print("Zero")
else:
    print("Non-Zero")




