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