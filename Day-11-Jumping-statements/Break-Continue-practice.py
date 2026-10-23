#1.Write a Python program to find and print the first prime number greater than 100. Use a loop and the break statement to exit the loop once you find the prime number.

for n in range(100,1000):
    for i in range(2,n):
        if n%i==0:
            break             
    else:
        print(f"First prime num greater than 100 is:{n}")
        break

# 2. Sum from 1 to 100, skipping numbers divisible by both 3 and 5
sumi=0
for n in range(1,101):
    if n%5==0 and n%3==0:
        continue
    sumi+=n
print(sumi)
    
   
# 3.Write a Python program to find and print the factors of a given number (input by the user). Use a loop and the break statement to exit the loop once you find all factors.

n=int(input("enter numbet to find factors:"))
print("Factors:",end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
    if i==n:
        break


#4.Average of a list, ignoring negative numbers
li=list(map(int,input().split()))
sumi=0
c=0
for i in range(len(li)):
    if li[i]>0:
        sumi+=li[i]
        c+=1
print(f"Average:{sumi/c}")

# 5.Create a Python program that simulates a basic login system. Ask the user to enter a username and password. If the entered password is incorrect, give the user three attempts. Use the break statement to exit the loop if the password is correct or the user exceeds the maximum attempts.

username = input("Enter username: ")
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if username == "rishitha" and password == "123456":
        print("Login successful!")
        break
    else:
        attempts += 1
        print(f"Invalid credentials. Attempts left: {3 - attempts}")

    if attempts == 3:
        print("Maximum attempts reached. Access denied!")
        break
 

#6.First 10 even numbers, skipping numbers divisible by 3
print("first 10 even numbers:",end='')
c=0
for i in range(2,100,2):#it gives even numbers only so we need to check the number which divisible by 3 and skip that iteration
    if i%3==0:
        continue
    print(i,end=" ")
    c+=1

    if c==10:
        break


print()

print("first 10 even numbers:",end='')
c = 0
for i in range(2, 100):#in this code we will get odd numbers also so we need to handle that case
    if i % 2 != 0:#here if i is odd then it will be skipped
        continue
    if i % 3 == 0:#if i is even and divisble by 3,it will bw skipped
        continue

    print(i, end=" ")
    c += 1

    if c == 10:
        break


# 7.Implement a program to calculate the factorial of a number entered by the user. Use a loop and the break statement to exit the loop when the calculation is complete.
n=int(input("enter number:"))
fact=1
i=1
while i<=n:
    fact*=i
    
    if i==n:
        break
    i+=1
print(fact)


#8.First 20 Fibonacci terms, stopping when a term exceeds 100
n=int(input("enter number:"))
c=2
a,b=0,1
print(f"fibonacci series: {a} {b}",end=" ")
for i in range(n-2):
    sumi=a+b
    if sumi>=100:
            break   
    print(sumi,end=" ")
    a,b=b,sumi
    c+=1
   

# 9.Create a Python program that asks the user to enter a series of numbers. Calculate and print the average of these numbers. If the user enters a negative number, stop taking input and calculate the average of the numbers entered so far using the break statement.
sumi=0
count=0
while True:
    n=int(input('enter number:'))
    if n>0:
        sumi+=n
        count+=1
    if n<0:
        break
print(f"Average: {sumi/count}")

# 10.Implement a Python program that counts and prints the number of vowels in a given string. Use a loop to iterate through the characters in the string and use the continue statement to skip consonants.

n=input("enter any string:")
vowel_c=0
for i in n:
    if i not in "AEIOUaeiou":
        continue
    vowel_c+=1
print(vowel_c)
        
# 11.Write a Python program to print all the prime numbers between 1 and 100. Use a loop and the break statement to exit the loop when you determine a number is not prime.

print(f"prime numbers 1-100: ",end=" ")
for n in range(2, 101):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, end=" ")
print()

#without nested for
print(f"prime numbers 1-100: ",end=" ")
for n in range(2, 101):
    i = 2

    while i < n:
        if n % i == 0:
            break
        i += 1

    if i == n:
        print(n, end=" ")

#12.Create a Python program that simulates a basic menu-driven application. The program should display a menu to the user with options like "Add," "View," and "Exit." Use the break statement to exit the loop when the user selects "Exit."
while True:
    print("1. Add")
    print("2. View")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Add selected")
    elif choice == 2:
        print("View selected")
    elif choice == 3:
        print("Exiting application...")
        break
    else:
        print("Invalid choice,Enter 1,2 or 3")

#13.Write a Python program that asks the user to input a password. If the password is not at least 8 characters long, keep asking for a valid password using a loop. Use the continue statement to skip further processing until a valid password is provided


while True:
    password=input("enter your password:")
    if len(password)<8:
        print("Password must be at least 8 characters!")
        continue
       
    print("It's a valid and strong password")
    break

#14.Write a Python program to find the sum of all even numbers from 1 to 100. However, if a multiple of 7 is encountered, skip it using the continue statement.
sumi=0
for i in range(0,101,2):#(1,101,2) if keep this range it will calculate sum of all odd numbers upto 100
    if  i%7==0:
        continue
    sumi+=i
print(sumi)
