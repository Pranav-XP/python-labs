#Solution to Lab 8
#program that works with loops in python

'''
Function 1 : Intro to loops
    function named looper which enters a loop and exists it as soon as the user writes "get me out of here"
    It should include instructions for the user.
'''

def looper():
    phrase = input("Enter a phrase.  Use the pharase -> get me out of here ")

    while (phrase != "get me out of here"): #continue to ask qiestion until phrase is not entered
        phrase = input("Enter another phrase.  Use the pharase -> get me out of here ") # Ask for another input

'''
Function 2 : Intro to loops and functions
    Function named cLooper which enters a loop and exists it as soon as  the user writes "get me out of here".
    It then returns the number of failed attempts the user made. 
'''

def cLooper():
    incorrect_attempts = 0
    phrase = input("Enter a phrase.  Use the pharase -> get me out of here ")

    while (phrase != "get me out of here"): #continue to ask qiestion until phrase is not entered
        incorrect_attempts +=1 # count the number of incorrect phrases entered
        phrase = input("Enter another phrase.  Use the pharase -> get me out of here ") # Ask for another input

    return incorrect_attempts

'''
Function 3 : Intro to loops, functions and lists
    Function named list_filler which fills a list with numbers  using a loop and exists it as soon as  the user writes "get me out of here".
    It then returns the filled list. 
'''

def list_filler():
    myList = []
    phrase = input("Enter some random numbers.  Use the pharase -> get me out of here ")
    
    while (phrase != "get me out of here"): #continue to ask qiestion until phrase is not entered
        myList.append(phrase) # add the phrase to the list
        phrase = input("Enter some more random numbers.  Use the pharase -> get me out of here ") # Ask for another input

    return myList


'''
Function 4: the main function that calls all other functions
'''
     
def main():

    # calling the looper function
    print("\n\nCaling the looper function\n\n")
    #looper()

    # calling the cLooper function
    print("\n\nCaling the cLooper function\n\n")
    result = cLooper()
    print ("result from cLooper is: ", result)


    # calling the list_filler function
    print("\n\nCaling the list_filler function\n\n")
    mylist = list_filler()
    print ("result from list_filler is: ", mylist)


main()
