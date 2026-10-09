# String basics
# - Creating strings
# - Single/double/triple quotes
# - Indexing
# - Negative indexing
# - Slicing
# - String immutability
# - len()
# - type()


# String built-in functions
# - len()
# - str()
# - ord()
# - chr()
# - ascii()

"""String Methods

upper()
lower()
capitalize()
title()
swapcase()


strip()
lstrip()
rstrip()

replace()
split()
rsplit()
join()

find()
rfind()
index()
rindex()
count()

startswith()
endswith()

isalpha()
isdigit()
isalnum()
isspace()
islower()
isupper()
istitle()


"""

# upper()
name = "rishitha"
print(name.upper())

# lower()
name = "RISHITHA"
print(name.lower())

# capitalize()
name = "rishitha"
print(name.capitalize())

# title()
name = "python programming"
print(name.title())

# replace()
text = "I like Java"
print(text.replace("Java", "Python"))

# split()
text = "Python is easy"
print(text.split())

# find()
text = "python programming"
print(text.find("program"))

# count()
text = "apple"
print(text.count("p"))

#swapcase()
s="RisHiTha"
print(s.swapcase())

#strip()--removes extra spaces from last and front
s="    rishitha janjirala "
print(s.strip())

#lstrip()--renoves left spaces and rstrip()--removes right space
s="      rishitha       j "
print(s.lstrip())



# rstrip()
s = "rishitha       "
print(s.rstrip())

#  rsplit()
s = "apple-banana-mango"
print(s.rsplit("-", 1))

# join()
words = ["Python", "is", "easy"]
print(" ".join(words))

# rfind()
s = "python programming python"
print(s.rfind("python"))

# index()
s = "python programming"
print(s.index("program"))

# rindex()
s = "python programming python"
print(s.rindex("python"))

#startswith()
s = "python programming"
print(s.startswith("python"))

# endswith()
s = "hello.py"
print(s.endswith(".py"))

# isalpha()
s = "Python"
print(s.isalpha())

# isdigit()
s = "12345"
print(s.isdigit())

# isalnum()
s = "Python123"
print(s.isalnum())

# isspace()
s = "   "
print(s.isspace())

# islower()
s = "python"
print(s.islower())

#  isupper()
s = "PYTHON"
print(s.isupper())

# istitle()
s = "Python Programming"
print(s.istitle())


