# #Elif statements:

# #1.Input three numbers and print the greatest among them.
# a=10
# b=20
# c=30
# if a>b and a>c:
#     print(f"{a} is greater among the numbers")
# elif b>c:
#     print(f"{b} is greater among the numbers")
# else:
#     print(f"{c} is greater among the numbers")


# #2.Take an input number and check whether it is a three-digit number.(if-else)
# n=int(input())
# if 100<= abs(n)<= 999:
#     print("Its three digit number")
# else:
#     print("Not a three digit number")


# # 3.Take temperature input and:
# # If above 30: print “It’s hot”
# # If between 15 and 30: print “Pleasant”
# # If below 15: print “Cold”
# temp=int(input("enter temp:"))
# if temp>30:
#     print("It's hot!!")
# elif temp >=15 and temp<=30:
#     print("Pleasant")
# else:
#     print("cold")

# #4.Check if a number is positive, negative, or zero.
# n=int(input("enter num:"))
# if n>0:
#     print(f"{n} is +ve num")
# elif n<0:
#     print(f"{n} is -ve num")
# else:
#     print(f"{n} is Zero")

# # 5. Take the user's marks and print:
# # A if 90 and above
# # B if 80 to 89
# # C if 70 to 79
# # D if 60 to 69
# # F if below 60
# marks=int(input("enter marks:"))
# if marks>=90:
#     print("Grade A")
# elif marks>=80 and marks<=89:
#     print("Grade B")
# elif marks>=70 and marks<=79:
#     print("Grade C")
# elif marks>=60 and marks<=69:
#     print("Grade D")
# else:
#     print("Grade F") 


# # 6.Input the number of sides and determine the type of polygon:
# # 3 → Triangle
# # 4 → Quadrilateral
# # 5 → Pentagon
# # Else → Unknown shape

# side=int(input("enter num of side:"))
# if side==3:
#     print("Triangel")
# elif side==4:
#     print("Quadrilateral")
# elif side==5:
#     print("Pentagon")
# else:
#     print("Unknown shape")


# # 7.Bus Fare:
# # Age < 5: "Free"
# # Age 5 to 18: "Half Ticket"
# # Age > 18: "Full Ticket"

# age=int(input("enter age:"))
# if age<5:
#     print("free")
# elif age>=5 and age<=18:
#     print("Half Ticket")
# else:
#     print("Full ticket")


# # 8.Student Grade Calculator:
# # If average marks > 90 → “Excellent”
# # Between 70-90 → “Good”
# # Below 70 → “Needs Improvement”

# avg_marks=int(input("enter marks:"))
# if avg_marks>90:
#     print("Excellent")
# elif avg_marks>70 and avg_marks<=90:
#     print("Good")
# else:
#     print("Needs Improvement")


# #9.Celsius to Fahrenheit or Fahrenheit to Celsius
# choice = input("Enter C or F: ")

# if choice == "C":
#     c = float(input("Enter Celsius: "))
#     f = (c * 9/5) + 32
#     print("Fahrenheit:", f)
# elif choice == "F":
#     f = float(input("Enter Fahrenheit: "))
#     c = (f - 32) * 5/9
#     print("Celsius:", c)
# else:
#     print("Invalid choice")


#10.simple calculator
a=int(input('enter val1:'))
b=int(input('enter val2:'))
operator=input("enter (-,*,+,/,//,%):")
if operator=="+":
    print("res:",a+b)
elif operator=="-":
    print("res:",a-b)
elif operator=="*":
    print("res:",a*b)
elif operator=="/":
    print("res:",a/b)
elif operator=="//":
    print("res:",a//b)
elif operator=="%":
    print("res:",a%b)
else:
    print("invalid operator")

#11.Guess number

import random
num=random.randint(1,10)
guess=int(input("enter a num between 1-10:"))

if guess==num:
    print("It's correct!!")
elif guess>num:
    print("Too low,The num was",num)
else:
    print("Too high,The num was",num)

#12.Password checker
password=input("enter ur password:")

if len(password) < 8:
    print("Weak password")
elif not any(ch.isdigit() for ch in password):
    print("Medium password: Add a digit")
else:
    print("Strong password")


#13.Greeting Based on Time of Day
hour = int(input("Enter hour (0-23): "))

if hour < 0 or hour > 23:
    print("Invalid hour")
elif hour < 12:
    print("Good morning!")
elif hour < 17:
    print("Good afternoon!")
elif hour < 21:
    print("Good evening!")
else:
    print("Good night!")

#14. Number of Days in a Month
month=int(input("enter month num(1-12):"))
if month==2:
    print("28 days")
elif month in (4,6,9,11):
    print("30 days")
elif month in (1,3,5,7,8,10,12):
    print("31 days")
else:
    print("invalid month,Given between 1-12")