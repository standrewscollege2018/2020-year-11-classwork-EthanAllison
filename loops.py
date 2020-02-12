"""This program is a simple fizz buzz code"""
number_1 = int(input("Pick a number\n"))
number_2 = int(input("Pick a number\n"))


if number_1 >number_2:
        start = number_2
        stop = number_1
else:
        start = number_1
        stop = number_2


for number in range (start,stop+1,1):
        print(number)

