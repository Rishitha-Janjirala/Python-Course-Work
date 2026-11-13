
#This code is without using any oop's concepts
balance = 10000
pin = 1234
attempts = 0

print("===== WELCOME TO ATM =====")

while attempts < 3:
    entered_pin = int(input("Enter your ATM PIN: "))

    if entered_pin == pin:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = 3 - attempts

        if remaining > 0:
            print("Incorrect PIN!")
            print("Remaining attempts:", remaining)
        else:
            print("Your ATM card is blocked!")
            print("Too many incorrect attempts.")

if attempts < 3 and entered_pin == pin:

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Available Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Deposit Successful!")
                print("Updated Balance:", balance)
            else:
                print("Invalid Amount!")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid Amount!")
            elif amount > balance:
                print("Insufficient Balance!")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining Balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM!")
            break

        else:
            print("Invalid Choice!")
