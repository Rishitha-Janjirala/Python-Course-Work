# Day 01 - Introduction to Programming & Python

# 1. Simple Python program
print("Hello, World!")

# 2. Python variables and values
name = "Rishitha"
age = 21
percentage = 85.5

print(name)
print(age)
print(percentage)

# 3. Procedural programming example
def login():
    print("Login")

def select_food():
    print("Select Food")

def payment():
    print("Payment")

login()
select_food()
payment()

# 4. Simple OOP example
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)

product = Product("Laptop", 50000)
product.display()

# Python is high-level, interpreted and general-purpose.
# Common applications: web development, automation, data science, AI/ML, scripting.
