#1.print 1-10
li=[i for i in range(1,11)]
print(li)

#2.Print even numbers
li=[i for i in range(1,11) if i%2==0]
print(li)

#3.print odd numbers
li=[i for i in range(1,11) if i%2==1]
print(li)

# 4.Find squares of numbers
li=[i**2 for i in range(1,11)]
print(li)

#method 2 taking list
li=[1,2,3,4,5]
res=[i**2 for i in li]
print(res)

# 4.Convert strings into lowercsae
l=['ABC',"DEF","SR"]
res=[i.lower() for i in l]
print(res)

# 5.Print numbers greater than 5
l=[2,4,7,9,10,24,6,4,12,3]
res=[i for i in l if i>5]
print(res)

#6.print +ve numbers
l=[1,2,4,-1,-3,4,-1]
res=[i for i in l if i>0]
print(res)

#7.Replace even numbers with EVEN and odd numbers with ODD
l=[1,2,3,4,5,6]
res=["EVEN" if i%2==0 else "ODD" for i in l]
print(res)

#8.Filter vowels from string
s='srthkiuytredfgmki'
res=[ch for ch in s if ch in 'aeiouAEIOU']
print(res)

# 9.Extract digits from string
s='1sdf3sdf6jhg01'
r=[ch for ch in s if ch.isdigit()]
print(r)

# 10.Common elements from two lists
a=[1,2,3,4]
b=[1,3,4,5]
r=[x for x in a if x in b]
print(r)