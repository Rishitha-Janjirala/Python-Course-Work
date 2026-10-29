# Functions:
# 1.Can you provide a simple function in Python without arguments and a return statement?
def greet():
    return "Hello"
print(greet())

# 2.How would you define a function with parameters in Python? Can you give an example?
def Add(a,b):
    return a+b
print(Add(10,20))

# 3.How can you create a function with a default parameter in Python? Can you provide an example?
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Rishitha")
# 4.How would you write a function with a docstring in Python? Can you show an example?

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print(add(10, 20))
print(add.__doc__)#add.__doc__ displays the function's docstring.


# For Scope
# 5.Can you provide an example to demonstrate local scope in Python?
def  display():
    name="srikar"
    print(name)
display()
# print(name) #NameError
# 6.How would you demonstrate enclosing scope in Python with an example?

a = 10  # Global
def outer():
    a = 20  # Enclosing
    def inner():
        print(a)
    inner()
outer()
    
# 7.Can you give an example to illustrate global scope in Python?
# A global variable is declared outside a function and can be accessed inside the function.
a = 10  # Global variable

def display():
    print(a)

display()
print(a)
# 8.How can you show built-in scope with an example in Python?
# Built-in scope contains predefined names in Python, such as print(), len(), sum(), and max().
numbers = [10, 20, 30, 40]

print(len(numbers))
print(sum(numbers))
print(max(numbers))

# Modifying and Accessing Variables

# 9.How would you modify a global variable from within a function in Python? Can you provide an example?
# We use the global keyword to modify a global variable inside a function.
a = 10

def modify():
    global a
    a = 20

modify()
print(a)

# 10.Can you show how to access a global variable from within a function in Python?
# We can access a global variable inside a function directly without using the global keyword, as long as we are only reading its value.
a = 100

def display():
    print(a)

display()

# 11.How can you modify a nonlocal variable in a nested function in Python? Can you give an example?
# We use the nonlocal keyword to modify a variable defined in an enclosing function.
def outer():
    a = 10

    def inner():
        nonlocal a
        a = 20

    inner()
    print(a)

outer()

# 12.How would you access a nonlocal variable in a nested function in Python? Can you provide an example?
# We can access a variable from an enclosing function directly inside a nested function without using the nonlocal keyword, as long as we only read it.
def outer():
    a = 50

    def inner():
        print(a)

    inner()

outer()