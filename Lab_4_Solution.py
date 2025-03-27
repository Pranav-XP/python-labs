#Solution to Lab 4
#program that works with Ratneels Kava Shop and Change Calculator

from graphics import * # we will be using this to create the user interface.

def main():

    # Exercise 1 of the lab is answered below
    # print a brief Welcome Message
    print("\tWelcome to Ratneels Kava Shop")
    print("\t-----------------------------")
    print("We sell the best quality kava in Fiji with a price of $2.50  per gram of kava")
    print() # print an empty line

    # get the input from the user
    # grams = float(input("How many Grams of Kava would you like to buy? "))
    grams = 10;
    
    # calculate the cost of kava
    cost_of_kava = grams * 2.50

    #display the cost of Kava
    print("The cost of your order is $", cost_of_kava)


    #Exercise 2 of the la is answered below
    #we will be extending functionality of ratneels Kava Shop Program
    
    # prompt user for amount tendered
    #amt_tendered = float(input("How much money has the customer tendered? "))
    amt_tendered= 30;

    #calculate appropriate change
    change = amt_tendered - cost_of_kava
    copy_change = change # this will be used to display in the user interface

    # display the amount of change to be returned
    print("your change is $", change)
    
    #calculate the denomination of change that need to be given
    # for this to be easy, we will convert change from dollars and cents to only cents
    change = change * 100 # convert change to cents

    num_20_dollars = change // 2000
    change = change - (num_20_dollars * 2000)
    
    num_10_dollars = change // 1000
    change = change - (num_10_dollars * 1000)

    num_5_dollars = change // 500
    change = change - (num_5_dollars * 500)
    
    num_1_dollars = change // 100
    change = change - (num_1_dollars * 100)

    num_50_cents = change // 50
    change = change - (num_50_cents * 50)

    num_20_cents = change // 20
    change = change - (num_20_cents * 20)

    num_10_cents = change // 10
    change = change - (num_10_cents * 10)

    num_5_cents = change // 5
    change = change - (num_5_cents * 5)

    #display each denomination of coin to be given
    print ("Number of $20.00 coin is ", num_20_dollars)
    print ("Number of $10.00 coin is ", num_10_dollars)
    print ("Number of $5.00 coin is  ", num_5_dollars)
    print ("Number of $1.00 coin is  ", num_1_dollars)
    print ("Number of $0.50 coin is  ", num_50_cents)
    print ("Number of $0.20 coin is  ", num_20_cents)
    print ("Number of $0.10 coin is  ", num_10_cents)
    print ("Number of $0.05 coin is  ", num_5_cents)
    
    #Creating the usr interface for this program
    win = GraphWin("Kava Shop", 400, 300) # create the interface
    win.setCoords(1.0,1.0,10.0,10.0) # # divide the interface into grids

    line1=Line(Point(1,0),Point(1,10))
    line1.draw(win)

    welcome_msg = Text(Point(2,0), "Ratneels Kava Shop")
    welcome_msg.draw(win)
    
    msg_1 = Text(Point(5,6), "The cost of Kava is :$" + str(cost_of_kava))
    msg_1.draw(win)
    
    msg_2 = Text(Point(5,4), "The amount tendered is :$" + str(amt_tendered))
    msg_2.draw(win)
    
    msg_3 = Text(Point(5,2), "your change is :$" + str(copy_change))
    msg_3.draw(win)

    win.getMouse()

    
    
    

main()
