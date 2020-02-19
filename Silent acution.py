"""This is a silent auction program that using error catching 19/2/2020"""

highest_name = ""
highest_bid = 0
error_catch = True



#asking for item for aiction
item = input("What is the auction for\n")
#setting up error catching
while error_catch == True:
#getting reserve price and checking to see if vaild input
    try:
        reserve_price = float(input("What is the reserve price\n"))
        if reserve_price >0.1:
            error_catch = False
        else:
            print("Enter a valid reserve price")
        
    except:
        print("Please remove the dollar sign")
        
    
    
#starting the auction and setting up error catching with the auction
print("The auction for the {} is underway".format(item))
error_catch = True
while error_catch == True:
#getting bidders name
    try:
        name = input("What is your bidder name\n")
        try:
#getting bidders bid
            bid = float(input("What is your bid\n"))
            
        except:
                print("Please remove the dollar sign")
#checking the bid to see if it is the highest bid    
        if bid >highest_bid:
            print("The highest bidder is {} with a bid of {}".format(name, bid))
            highest_bid = bid
            highest_name = name
#setting -1 to end the auction
        elif bid == -1:
            error_catch = False
        else:
            print("This bid does not exceed the highest bid, please enter a higher amount")
            

    except:
        print("This is not a valid number, please enter again")



#checking the highest bid to see if it has reached the reserve price 
if highest_bid >=reserve_price:
    print("The Auction has ended, {} has won with a bid of {}".format(highest_name, highest_bid))
else:
    print("The {} has not reached the reserve price and hasn't been sold".format(item))
        

      

