#Solution to Lab 8
#program that works with decision making in python


'''
unction called “cus_classify”
    The function should take one parameter which is the customer account balance.
    The function should return the classification of the customer, that is, the function should return “Rich”
    if the customer balance is more than 10, 000 FJD, otherwise, it should return “Poor”.
'''

def cus_classify(balance):
    classification = ""
    # the “if” statement that classify the user into one of two different classifications
    if balance > 10000 :
        classification = "Rich"
    else:
        classification = "Poor"

    return classification #return the classification



'''
main function that does everthing
'''
     
def main():
    #----------------------------------------------------------
    # Exercise 1 of the lab is answered below -> Creating lists  
    #----------------------------------------------------------
    print ("\nExercise Python Lists of the lab is answered below\n")
    
    cus_classification = ""
    
    AccBalance = float(input("\nEnter your bank account balance for customer 1: \t$")) # get input form user for customer account balance
    # the “if” statement that classify the user into one of two different classifications
    if AccBalance > 10000 :
        cus_classification = "Rich"
    else:
        cus_classification = "Poor"
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.


    AccBalance = float(input("\nEnter your bank account balance for customer 2: \t$")) # get input form user for customer account balance
    # the “if” statement that classify the user into one of two different classifications
    if AccBalance > 10000 :
        cus_classification = "Rich"
    else:
        cus_classification = "Poor"
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.


    AccBalance = float(input("\nEnter your bank account balance for customer 3: \t$")) # get input form user for customer account balance
    # the “if” statement that classify the user into one of two different classifications
    if AccBalance > 10000 :
        cus_classification = "Rich"
    else:
        cus_classification = "Poor" 
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.


    AccBalance = float(input("\nEnter your bank account balance for customer 4: \t$")) # get input form user for customer account balance
    # the “if” statement that classify the user into one of two different classifications
    if AccBalance > 10000 :
        cus_classification = "Rich"
    else:
        cus_classification = "Poor"   
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.


    AccBalance = float(input("\nEnter your bank account balance for customer 5: \t$")) # get input form user for customer account balance
    # the “if” statement that classify the user into one of two different classifications
    if AccBalance > 10000 :
        cus_classification = "Rich"
    else:
        cus_classification = "Poor" 
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

        
    
    #--------------------------------------------------------------
    # Exercise 2 of the lab is answered below -> Python Functions  
    #--------------------------------------------------------------
    print ("\n\n\nExercise Revisiting function of the lab is answered below\n")
    # Within the main function, remove the if statement and instead, call your function “cus_classify” and print the classification of the customer

    AccBalance = float(input("\nEnter your bank account balance for customer 1: \t$")) # get input form user for customer account balance
    cus_classification = cus_classify(AccBalance)
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

    AccBalance = float(input("\nEnter your bank account balance for customer 2: \t$")) # get input form user for customer account balance
    cus_classification = cus_classify(AccBalance)
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

    AccBalance = float(input("\nEnter your bank account balance for customer 3: \t$")) # get input form user for customer account balance
    cus_classification = cus_classify(AccBalance)
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

    AccBalance = float(input("\nEnter your bank account balance for customer 4: \t$")) # get input form user for customer account balance
    cus_classification = cus_classify(AccBalance)
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

    AccBalance = float(input("\nEnter your bank account balance for customer 5: \t$")) # get input form user for customer account balance
    cus_classification = cus_classify(AccBalance)
    print ("This customer is classified as : ", cus_classification )#Print the customers classifications.

    

main()
