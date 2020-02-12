age = int(input("How old are you?\n"))
if age > 13:
    student = input("Are you a student? (y/n)\n")
    if student == "y":
        print("It costs $8")
    elif age >= 18:
        print("It will cost $12")
    else:
        print("It will cost $9")
elif age >=5:
    print("It will cost $7")
else:
    print("It will be free to enter")
    
