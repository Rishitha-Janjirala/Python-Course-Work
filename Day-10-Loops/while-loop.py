#1.Counting: Write a while loop that counts from 1 to 10 and prints each number.
n=int(input("enter num:"))
i=1
while i<=n:
    print(i)
    i+=1

# 2.Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.
n=int(input("enter number:"))
while n>=1:
    print(n)
    n-=1

#3.Write a while loop that calculates the sum of even numbers from 1 to 100.
i=1
sumi=0
while i<=100:
    if i%2==0:
        sumi+=i
    i+=1
print(sumi)

#4.Create a simple number guessing game using a while loop. Generate a random number and have the user guess it, giving hints like "too high" or "too low" until they guess correctly.

import random
n=random.randint(1,100)
guess=int(input("guess a num between 1-100:"))

while guess!=n:
    if guess > n:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

    guess = int(input("Guess again: "))

print("Congratulations! You guessed correctly.")


#5.Use a while loop to calculate the factorial of a given number.
n=int(input("enter number:"))
fact=1
# i=1 #without this
while n>0:  #i<=n
    fact=fact*n #fact*=i
    n-=1  #if we use i -- i+= 1
print(fact)


#6.Write a while loop that prints all even numbers between 1 and 50.
i=1
while i<=50:
    if i%2==0:
        print(i,end=" ")
    i+=1

#method/way 2
i = 2
while i <= 50:
    print(i)
    i += 2

#7.Create a program that calculates the sum of the digits of a given integer using a while loop.

n=int(input("enter number:"))
sumi=0
while n>0:
    rem=n%10
    sumi+=rem
    n//=10
print("sum of digits is:",sumi)

# 8.Generate a multiplication table for a given number using a while loop.
n=int(input("enter num:"))
i=1
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1

# 9.Write a program to find all the factors of a given number using a while loop.
n=int(input("enter num:"))
i=1
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i+=1

# 10.Implement a program that reverses even numbers using a while loop.

n = int(input("Enter even number: "))
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

print("Reversed number:", rev)
