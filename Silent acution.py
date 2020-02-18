"""This is a silent auction program that using error catching 19/2/2020"""

highest_name = ""
highest_bid = 0
error_catch = True




item = input("What is the auction for\n")
while error_catch == True:
    try:
        reserve_price = int(input("What is the reserve price\n"))
        error_catch = False
    except:
        print("Please remove the dollar sign")
        
    
    

print("The auction for the {} is underway".format(item))
error_catch = True
while error_catch == True:
    try:
        name = input("What is your bidder name\n")
        try:
            bid = float(input("What is your bid\n"))
        except:
                print("Please remove the dollar sign")
        
        if bid >highest_bid:
            print("The highest bidder is {} with a bid of {}".format(name, bid))
            highest_bid = bid
        else:
            print("This bid does not exceed the highest bid, please enter a higher amount")
            

    except:
        print("This is not a valid number, please enter again")
        

      

