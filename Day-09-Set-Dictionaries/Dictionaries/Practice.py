#1.Create a dictionary to store five subject names and their marks.

dict={  
   "Python":90,
    "Java":85,
    "Maths":80,
    "English":95,
    "Chemistry":98

}
print(dict)

#2.Print only the keys from a dictionary whose values are greater than 90
for key,val in dict.items():
    if val>=90:
        print(key)
