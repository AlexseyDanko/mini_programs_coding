import random

number = random.randrange(1, 10)
trying_to_guess = int(input("Enter any number: "))
while number != trying_to_guess:
    if trying_to_guess < number:
        print("Too low")
        trying_to_guess = int(input("Enter number again: "))
    elif trying_to_guess > number:
        print("Too high!")
        trying_to_guess = int(input("Enter number again: "))
    else:
        break
print("you guessed it right!!")
