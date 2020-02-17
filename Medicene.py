""" This program shows how much medicene to give to a patient 12/2/2020"""
#setting values for max and min numbers for age and weight
AGE_LIMIT = 12
WEIGHT_MIN = 1
WEIGHT_MAX = 200



#asking user for their age
age = int(input("What is your age?\n"))
    #checking to see if user is over 12 to give them 2 tablets
if age >= AGE_LIMIT:
              print("You may have two 500mg tablets")
    #asking user for their weight because they are under 12

else:
    weight = int(input("How much does your child weight?\n"))
        #checking users weight and setting bountries to see if they are messing around 
if weight < WEIGHT_MIN:
    print("This weight is not allowed")

elif weight > WEIGHT_MAX:
    print("This weight is not allowed")
        #Multipling the users weight by 10 to see how much paracetamol they can have
dose = (weight * 10)
print("Your child is allowed {} millgrams of paracetamol".format(dose))

    
