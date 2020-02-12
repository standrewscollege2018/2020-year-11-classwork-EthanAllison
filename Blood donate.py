""" This is a program using inputs and conditionals to figure out wether you can donate blood 11/2/2020"""
#Setting miniuim age and weight
MIN_AGE = 16
MIN_WEIGHT = 50

#asking the user what their age and weight are?
age = int(input("How old are you?\n"))
weight = int(input("How much do you weigh?\n"))

#Checking users age and weight againest the minimum age and weight and responding with different respondes

if age >=MIN_AGE and weight >=MIN_WEIGHT:
    print("You are eligible to donate blood, please take a seat over there.")
else:
    print("Sorry, you are not eligible to donate blood at this time.")

    
