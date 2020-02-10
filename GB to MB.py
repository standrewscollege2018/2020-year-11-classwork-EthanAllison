"""To find out the number of megabytes in a gigabytes using the .format layout."""

#GB is 1024 megabytes which is a constant 
GB = 1024

#input
gb = int(input("Number of Gigabytes"))

#output
print("There are {}{} megabytes in {}".format(gb * GB, gb))







