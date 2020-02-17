""" This is a looped program that allows you to add different names 17/02/2020"""
#getting how many names the user wants

num_names = int(input("How many names do you want\n"))

#setting the number of times they want a name to read 
for num_names in range (0,num_names,1):
    name = input("Enter a name\n")
#printing the names
    print("Hello", name)




