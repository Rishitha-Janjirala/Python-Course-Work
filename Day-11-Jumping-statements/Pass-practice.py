# 1.Create a Python program that iterates over a list of integers and prints all even numbers. For odd numbers, use the pass statement to do nothing.

arr=list(map(int,input('Enter numbers: ').split()))
print("even numbers:",end=" ")
for num in arr:
    if num%2==0:
        print(num,end=' ')
    else:
        pass

# 2.Write a Python program that asks the user to input a list of numbers. For each number in the list, check if it's a prime number. If it's prime, print it; if not, use the pass statement.
        
li=list(map(int,input("enter numbers:").split()))
print("Prime numbers:",end=" ")
for n in li:
    f_c=0
    for i in range(1,n+1):
        if n%i==0:
            f_c+=1
    if f_c==2:
        print(n,end=" ")
    else:
        pass
   
# 3.Implement a Python program that simulates a basic class structure for a geometric shape. Create a class named Shape, and for now, use the pass statement to indicate that further methods need to be added in the future.

class shape:
    pass
shape1=shape()
print("shape obj created")


# 5.Write a Python program that reads a text file and counts the number of lines that contain the word "apple." For lines that don't contain the word, use the pass statement.

count=0
with open("sample.txt", "r") as file:
    for line in file:
        if "apple" in line:
            count+=1
        else:
            pass
print(count)


# 6.Create a Python program to check if a given number is a perfect square. If it is, print a message; otherwise, use the pass statement.

#using for loop
n = int(input("Enter number: "))
for i in range(1, n + 1):
    if i * i == n:
        print(f"{n} is a perfect square")
        break
else:
    pass
    print(f"{n} is not a perfect square")  

# 6.Create a Python program that defines a class called Employee. Use the pass statement to indicate that you need to define attributes and methods for the class later.
class employee():
    pass

emp1=employee()
print("employee class and object is created succesfully")

# 7.Write a Python program to iterate through a list of sentences and check if each sentence ends with a question mark. If it does, print the sentence; otherwise, use the pass statement.

sentences = []

print("Enter sentences:")

while True:
    s = input()
    if s == "":
        break
    sentences.append(s)

for s in sentences:
    if s.endswith("?"):
        print(s)
    else:
        pass


# 8.Implement a Python program that iterates through a list of tasks. For each task, check if it's completed. If it's completed, print a message; if not, use the pass statement.

tasks = [
    ("Study Python", True),
    ("Complete assignment", False),
    ("Practice coding", True),
    ("Read notes", False)
]

print("Completed tasks:")

for task, status in tasks:
    if status == True:
        print(task)
    else:
        pass