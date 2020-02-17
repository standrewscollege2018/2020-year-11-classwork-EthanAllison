"""This is a program that guesses a number using while loops 17/2/2020"""
#setting constants
import random
number = random.randint(1,10)

keep_asking = True
while keep_asking == True:
    guess = int(input("Guess a number between 1 and 10\n"))

    if guess == number:
        keep_asking = False
    elif guess >number:
        print("Your guess is to high, guess lower")
    else:
        print("Your guess is to low, guess higher")
    

print("Correct the number is", number)
