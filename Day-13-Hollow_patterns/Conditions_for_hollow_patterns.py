#pattern
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

#condition for 1st row -->i==0
n=5
for i in range(n):
    for j in range(n):
        if i==0:
            print("*",end=" ")
    print()

#condition for last row -->i==n-1
n=5
for i in range(n):
    for j in range(n):
        if i==n-1:
            print("*",end=" ")
    print()
            


#condition for 1st column -->j==0
n=5
for i in range(n):
    for j in range(n):
        if j==0:
            print("*",end=" ")
    print()

#condition for last column -->j==n-1
n=5
for i in range(n):
    for j in range(n):
        if j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()


#condition for left daigonal -->i==j
n=5
for i in range(n):
    for j in range(n):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#condition for right daigonal -->i+j==n-1 or j=n-i-1
n=5
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#condition for middle row --> n//2
n=5
for i in range(n):
    for j in range(n):
        if i==n//2:
            print("*",end=" ")
        else:
            print(" ",end=' ')
    print()


#condition for middle column --> n//2
n=5
for i in range(n):
    for j in range(n):
        if  j==n//2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()