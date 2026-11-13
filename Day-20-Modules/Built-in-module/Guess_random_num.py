import random as r

num=r.randint(1,100)
attempts=0

print("===== NUMBER GUESSING GAME =====")
print("Guess a number between 1 and 100")


while attempts<3:
    guess=int(input("Enter your guess: "))
    attempts+=1

    if guess<num:
        print("Too low! Try a bigger number")

    elif guess>num:
        print("Too high! Try a smaller number")

    else:
        print("Kudoos...!")
        print("The number was:",num)


print("You attempts Exceeded")
print("The number is:",num)
        
