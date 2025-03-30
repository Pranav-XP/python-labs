#Solution to Lab 5
#program that works with Strings and lists


def main():
    #---------------------------------------------------------------
    # Exercise String Mainipulation of the lab is answered below
    #---------------------------------------------------------------
    print ("\nExercise String Manipulation of the lab is answered below\n")

    myString = "This is my Python string"
    
    #a. determine and print the number of characters present in “myString”

    print ("Number of characters in myString is: ", len(myString))

    #b. print only the first character of the words present in your string (hint: Use string indexes to do this)

    print ("\nFirst characters of words in myString are: ")
    print (myString[0])
    print (myString[5])
    print (myString[8])
    print (myString[11])
    print (myString[18])
    
    #c. print the first word in myString (hint: use substring to achieve your output)

    print ("\nFirst word in myString is: ")
    print (myString[0: 4: 1]) # string[start: end: step]



    #---------------------------------------------------------------
    # Exercise Python Lists of the lab is answered below
    #---------------------------------------------------------------
    print("\n\nExercise Python Lists of the lab is answered below\n")
    myList = myString.split(" ") # list generated from splitting teh string at " " or space

    # Use a definite for loop to print all the elements inside the your “myList” variable
    print("Printing all elements in the list")
    for item in myList:
        print (item)

    # Update your list by removing the word “my” present inside the list and replacing it with the word “our”.
    myList[2] = "our"
    print("\nPrinting all elements in the list again")
    for item in myList:
        print (item)

    # Create a new variable called “ourString”.  The purpose of this new variable is to include all the elements inside “myList” 
    # in a simple string.
    ourString = "" # created empty string

    for item in myList: #use a for loop to join all elements of list back into a string
        ourString = ourString + item + " "

    print("\nPrinting ourString")
    print (ourString)
        

main()
