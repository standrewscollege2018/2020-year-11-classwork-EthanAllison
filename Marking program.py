""" This is a program that will use elifs and conditionals to mark a paper and give back the grade 12/2/2020"""

#asking the user for the students grade
score = int(input("What is the students final grade?\n"))

#checking the score to see what grade they got
if score >=7:
    print("Congratulations you have got an Excellence on your paper")
elif score >=5:
    print("Well down you got a Merit on your paper")
elif score >=3:
    print("You did ok and got an Achieved on your paper")
else:
    print("You have not achieved on your paper, see me after class")

