#1.Print numbers from 1 to 5 using a for loop
n=int(input("enter val:"))
for i in range(1,n+1):
    print(i)

#2.Print even numbers between 1 and 10
n=int(input("enter num:"))
for i in range(1,n+1):
    if i%2==0:
        print(i,end=" ")
    
#3.Print multiplication table of a number
n=int(input("enter number:"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#4.Print all characters of a string
string=input("enter str:")
for ch in string:
    print(ch)

#4.print vowels from string
string=input("enter str:")
for ch in string:
    if ch in "aeiouAEIOU":
        print(ch,end=' ')
    
#5.print consonents from string
string=input("enter str:")
for ch in string:
    if ch not in "aeiouAEIOU":
        print(ch,end=' ')

#6.print the count of vowels from string.

string=input("enter str:")
vowel=0
for ch in string:
    if ch in "aeiouAEIOU":
        vowel+=1
print(f"count of vowel:{vowel}")


#7.Find the factors of a number 
n=int(input("enter number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")

#8.Print factorial of a number
n=int(input("enter number:"))
fact=1
if n<0:
    print("no factorail for -v numbers")
else:
    while n>0:
        fact*=n  #fact=fact*num
        n-=1    #n=n-1
    print("factoial:",fact)

#using recursive function
def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter num:"))
print(f"factorial of {n}:",fact(n))


#9.Print squares of numbers from 1 to n
n=int(input("enter number:"))
for i in range(1,n+1):
    print(i**2,end=" ")

#10.Check if a number is prime
n=int(input("enter number:"))
f_c=0
for i in range(1,n+1):
    if n%i==0:
        f_c+=1
if f_c==2:
    print("Prime number")
else:
    print("Not prime number")

#11.Calculate the sum of numbers from 1 to 10 using a for loop ?
n=int(input("enter num:"))
sumi=0
for i in range(1,n+1):
    sumi+=i
print(sumi)

#12.Find the maximum value in a list using a for loop ?
li=list(map(int,input("enter list of elemnts:").split()))
maxi=0
for i in li:
    if i>maxi:
        maxi=i
print(f"max ele in list is: {maxi}")

# 13.Print Even Numbers from 1 to 10
n=int(input("enter num:"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

# 14.Print Elements of a List-intergers
li=list(map(int,input("enter list:").split()))
n=len(li)
for i in range(n):
    print(li[i])

#for string list input
li=input().split()
n=len(li)
for i in range(n):
    print(li[i])
    
#15.Find maximum value in a list
li=list(map(int,input().split()))
maxi=0
for i in range(len(li)):
    if li[i]>maxi:
        maxi=li[i]
print(maxi)


# 16.Common Elements Between Two Lists
l1=list(map(int,input("enter list1:").split()))
l2=list(map(int,input("enter list2:").split()))

for i in l1:
    for j in l2:
        if i==j:
            print(i)

#17.Reverse a string
string=input("enter string:")
n=len(string)
for i in range(n-1,-1,-1):
    print(string[i],end='')

#18.Generate a list of squares for numbers from 1 to 10 using a for loop.
n=int(input("enter number:"))
li=[]
for i in range(1,n+1):
    li.append(i**2)
print(li)

#19.Count the number of words in a sentence using a for loop.
n=input()
words=1
for i in range(len(n)):
    if n[i]==" ":
        words+=1
print(words)


# 20.Calculate the power of a number using a for loop.
base=int(input("enter base:"))
expo=int(input("enter exponent:"))

res=1
for i in range(expo):
    res=res*base
print(res)

# base=int(input("enter base:"))
# expo=int(input("enter exponent:"))

# print("res:",base**expo)

# #20.print prime numbers from 1-100
print("primes numbers:",end="")
for i in range(1, 100):
    fc = 0
    for j in range(1, i + 1):
        if i % j == 0:
            fc += 1

    if fc == 2:
        print(i,end=" ")