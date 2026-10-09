#1. Count vowels in a string
s="Rishitha"
c=0
for ch in s:
    if ch in "aeiouAEIOU":
        c+=1
print(f"count of vowels:{c}")

#2.Count Spaces
s="Welcome Pfs Batch 69"
c=0
for ch in s:
    if ch==" ":
        c+=1
print(f"count of spaces:{c}")

#3.Reverse string
s="Rishi"
print(s[::-1])

#4.Check palindrome
s="mam"
if s==s[::-1]:
    print("palindrome")
else:
    print("Not palindrome")

#5.Convert first letter of every word to uppercase
s="Hello welcome to codegnan"
print(s.title())



