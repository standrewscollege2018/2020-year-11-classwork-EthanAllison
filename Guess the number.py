"""This is a program that guesses a number using while loops 17/2/2020"""
#Getting random number

import random
number = random.randint(1,10)

#setting loop
error_catch = True
while error_catch == True:
#Asking user to guess the number and checking to see if they are correct
#error catching
    try:
        guess = int(input("Guess a number between 1 and 10\n"))
        if guess in range (1,10):
            if guess == number:
                error_catch = False
            elif guess >number:
                print("Your guess is to high, guess lower")
            else:
                print("Your guess is to low, guess higher")
        else:
            print("Are you 5, that's not a number between 1 and 10 dumbass")
              
    except:
        print("Retard that isn't a number")
        
#if they get it correct
print("Correct the number is", number)
