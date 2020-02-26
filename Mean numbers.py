"""This program uses loops and lists to display numbers"""
numbers = []
keep_asking = True

while keep_asking == True:
    try:
        num = int(input("Enter a number\n"))
        if num == -1:
            keep_asking = False
        else:
            numbers.append(num)
    except:
        print("Invalid number, please enter again")
        
print("You entered these numbers")
for i in range(len(numbers)):
    print(numbers[i])
print("The mean of these numbers are",sum(numbers)/len(numbers))
        


    
