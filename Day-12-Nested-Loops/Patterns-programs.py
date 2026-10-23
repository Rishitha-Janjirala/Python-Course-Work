#1.n*m square pattern
n=int(input('enter numer:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()

# pattern-2
# 1 2 3
# 1 2 3
# 1 2 3
for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()

#method-2
for i in range(1,4):
    c=1
    for j in range(1,4):
        print(c,end=' ')
        c+=1
    print()

#pattern-3
# 1 1 1 
# 2 2 2 
# 3 3 3
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()

#method-2
c=1
for i in range(1,4):
    for j in range(1,4):
        print(c,end=' ')
    c+=1
    print()

#pattern-4
# 1 2 3 
# 4 5 6 
# 7 8 9
c=1
for i in range(1,4):
    for j in range(1,4):
        print(c,end=' ')
        c+=1
    print()

#pattern-5-right angle triangle
n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print('*',end=' ')
    print()

#pattern-5 
#     *
#   * *
# * * *
n=4
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=' ')
    for j in range(i):
        print('*',end=' ')
    print()

#pattern-6
# * * *
# * *
# *
r=4
for i in range(1,r+1):
    for j in range(1,r):
        print("*",end=' ')
    r-=1
    print()

#pattern-7
# * * *
#   * *
#     *
n=3
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=' ')
    for j in range(i):
        print('*',end=' ')

    print()

#pattern-8 --pyramid
n=3
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=' ')
    for j in range(2*i-1):
        print("*",end=' ')
    print()

#pattern-9
# A B C
# A B C
# A B C
for i in range(3):
    for j in range(65,68):
        print(chr(j),end=" ")
    print()

#pattern-10
# A A A
# B B B 
# C C C
for i in range(65,68):
    for j in range(3):
        print(chr(i),end=' ')
    print()


#pattern-11
# A B C 
# D E F 
# G H I
n=65
for i in range(3):
    for j in range(3):
        print(chr(n),end=" ")
        n+=1
    print()
    

