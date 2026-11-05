#Recursion
# 1.Write a Python function to calculate the factorial of a given number using recursion.
def fact(n):
    if n==0 or n==1:
        return  1
    return n*fact(n-1)
print(fact(5))

# Write a Python function to generate the nth Fibonacci number using recursion.
def fibo(n):
    if n==0 or n==1:
        return n
    return fibo(n-2)+fibo(n-1)
print(fibo(5))

# Write a Python function to calculate the sum of digits of a given number using recursive functions.
def sumi_digits(n):
    if n==0 or n==1:
        return n
    return n%10 + sumi_digits(n//10)
print(sumi_digits(12))

# Print the Pattern by using recursive Function
# n=5
#  Output: 54321012345
def pattern(n):
    if n<0:
        return
    print(n,end='')
    pattern(n-1)
    if n!=0:
        print(n,end='')
        
pattern(5)


# Find the sum of the elements in the given list by using recursive Function
# L = [1,2,3,4,5,6]
#  Output: 21
def sum_list(L, n):
    if n == 0:
        return 0

    return L[n-1] + sum_list(L, n-1)

L = [1,2,3,4,5,6]
print(sum_list(L, len(L)))

# Convert nested list into single list by using recursive function
# L = [[1,2,3],4,[5],[6,7,8,9],10]
#  Output: [1,2,3,4,5,6,7,8,9,10]
def flatten(L):
    result = []

    for i in L:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

L = [[1,2,3],4,[5],[6,7,8,9],10]
print(flatten(L))


# Print n even numbers by using recursive Function
# Input: 5
#  Output: 0,2,4,6,8
def even(n, i):
    if i == n:
        return

    print(2*i, end=" ")
    even(n, i+1)

n = int(input("Enter n: "))
even(n, 0)

# Print n odd numbers by using recursive Function
# Input: 5
#  Output: 1,3,5,7,9
def odd(n, i):
    if i == n:
        return

    print(2*i+1, end=" ")
    odd(n, i+1)

n = int(input("Enter n: "))
odd(n, 0)

# Find the Sum of the given number by using recursive Function
# Input: 12345
#  Output: 15
def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)

n = int(input("Enter number: "))
print(digit_sum(n))
