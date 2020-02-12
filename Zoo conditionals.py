"""This is a program to show how to use conditionals to detect if a person pays the child price or not 11/2/2020"""
#setting the child age limit
CHILD_AGE = 13
#getting the age from the user
#use int() to compare to CHILD_AGE to use a number for input 
age = int(input("How old are you kid \n"))
#Checking the users age wether they can pay the child price or not
if age <=CHILD_AGE:
    print("You may pay the child price of $10")
else:
    print("You have to pay the full price of $20. Sorry")
#printing text allowing them into the Zoo 
print("Welcome to the zoo")

