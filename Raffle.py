"""This is a raffle"""
import random
import time

raffles = []

keep_asking = True
while keep_asking == True:
    try:
        prize_name = input("Enter the prize name\n")
        keep_asking = False
        if prize_name =="":
            print("Invalid prize name, Enter again")
    except:
        print("Invalid prize name, Enter again")


get_price = True
while get_price == True:
    try:
        prize_num = int(input("Enter the prize price\n"))
        get_price = False
    except:
        print("Invalid prize price, enter again")

keep_asking = True 
while keep_asking == True:

    try:
        raffle = input("Enter your name for the raffle\n")
        if raffle == "admin":
            keep_asking = False
        elif raffle == "":
            print("Dumbass Benji stop pressing enter, you cocksucker")
        else:
            raffles.append(raffle)
    except:
        print("Invalid data, please enter again")

print("Here are names in the raffle, Good Luck everybody")
for i in range(len(raffles)):
    print(raffles[i])
print("The winner will now be drawn")
time.sleep(1)
print("Drawing...")
time.sleep(2)
print("The winner is {}, they have won {} with the value of {}".format(random.choice(raffles),prize_name,prize_num))

    

