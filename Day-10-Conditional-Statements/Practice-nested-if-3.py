# NESTED IF STATEMENT

# 1.Given x = 10 and y = 5, write a Python program to determine if x is greater than y. If x is greater than y, check if it's also greater than 15 and print appropriate messages accordingly.

x=10
y=5
if x>y:
    print("x is greater than y")
    if x>15:
        print("x is greater than y and 15 also")
    else:
        print("x is not greater than 15")
else:
    print("x is not greater than y")


# 2.Write a Python program to check if a person is eligible for a credit card based on their age and income. If the person is underage, print "You are underage." If they are of age but have an income below $30,000, print "Your income is too low for a credit card."

age=int(input("enter ur age:"))
income=int(input("enter ur invome:"))
if age>=20:
    if income>=30000:
        print("You are eligible for a credit card.")
    else:
        print("Your income is too low for a credit card.")
else:
    print("You are underage")

#3.Write a Python program to determine whether a number is even or odd. If it is even, check whether it is greater than 10.
num=int(input("enter num:"))
if num%2==0:
    if num>10:
        print(f"{num} is even and greater than 10")
    else:
        print(f"{num} is even but not greater than 10")
else:
    print(f"{num} is odd")

#4.Write a Python program that calculates the ticket price for a theme park based on age and height. If a person is under 12 years old and under 4 feet tall, the ticket price is $10. If they are under 12 but 4 feet tall or taller, the ticket price is $15. If a person is 12 or older and under 4 feet tall, the ticket price is $15. If they are 12 or older and 4 feet tall or taller, the ticket price is $20.
age=int(input("enter age:"))
height=float(input("enter height:"))

if age<12:
    if height < 4:
        print("Ticket price is $10")
    else:
        print("Ticket price is $15")
else:
    if height < 4:
        print("Ticket price is $15")
    else:
        print("Ticket price is $20")


#5.Write a Python program for user authentication. Ask the user to enter their username and password. If both the username and password are correct, print "Access granted." If the username is correct but the password is incorrect, print "Incorrect password." If the username is incorrect, print "Invalid username."
user_name=input("enter username:")
password=int(input("enter pasword:"))
if user_name=="Admin":
    if password==1234:
        print("Access granted")
    else:
        print("Invalid password")
else:
    print("Inavlid Username")

#6.Write a Python program for ordering food. Ask the user to select a type of food (e.g., "Burger" or "Pizza"). If they choose "Burger," ask if they want fries. If they choose "Pizza," ask if they want extra cheese. Print their order with the additional items if chosen.
food=input("choose Burger or pizza")
if food=="Burger":
    fries=input("do you add fries?(Y/N):")
    if fries == "Y":
        print("Your order: Burger with fries")
    else:
        print("Your order: Burger")
elif food == "Pizza":
    cheese = input("Do you want extra cheese? (Y/N): ")

    if cheese == "Y":
        print("Your order: Pizza with extra cheese")
    else:
        print("Your order: Pizza")

else:
    print("Invalid food choice")
