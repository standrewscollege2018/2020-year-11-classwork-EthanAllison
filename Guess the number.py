"""This is a program that guesses a number using while loops 17/2/2020"""
#Getting random number
import random
number = random.randint(1,10)
#setting loop
keep_asking = True
while keep_asking == True:
#Asking user to guess the number
    guess = int(input("Guess a number between 1 and 10\n"))
#Checking wether it is correct or not 
    if guess == number:
        keep_asking = False
    elif guess >number:
        print("Your guess is to high, guess lower")
    else:
        print("Your guess is to low, guess higher")
    
#if they get it correct
print("Correct the number is", number)
