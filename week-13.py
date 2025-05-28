# Lab Week 13 template.
# Below is a definition of a class, and a short script that uses that class.
# Read it carefully and understand what it is doing.
# Run the script and see what happens.
# The reason it gives an error is that a call is made to a method
# That does not exist.
# In more detail: The class NaturalNumber has four method. A constructor,
# and the methods get(), isEven(), and isSquare().
# As you should see, the script invokes there three methods.
# But it also invokes the method isPrime(). That method is not defined.
# You task is to add the method isPrime to the class definition and
# write its code so it correctly checks for primality.
# You must not alter any other method.
# You must not alter the main.



class NaturalNumber:
    def __init__(self, n):
        self.n = n

    def get(self):
        return self.n

    def isEven(self):
        return self.n % 2 == 0

    def isSquare(self):
        for k in range(1, self.n):
            if self.n == k ** 2:
                return True
        return False
    
    def isPrime(self):
        prime = True
        # If given number is greater than 1 
        if self.n > 1:  
            # Iterate from 2 to n / 2  
            for i in range(2, self.n): 
                # If num is divisible by any number between  
                # 2 and n / 2, it is not prime  
                if (self.n % i) == 0: 
                    prime =  False
                    break
          # if number is less than 1
        else: 
          prime = False

        return prime;



def main():

    print("This script get a number and checkes some of its attributes.")
    print()

    n = eval(input("Enter a natural number: "))
    num = NaturalNumber(n)

    if num.isEven():
        print("The number {0} is even.".format(num.get()))
    else:
        print("The number {0} is odd.".format(num.get()))

    if num.isSquare():
        print("The number {0} is a square number.".format(num.get()))
    else:
        print("The number {0} is not a square number.".format(num.get()))

    if num.isPrime():
        print("The number {0} is a prime number.".format(num.get()))
    else:
        print("The number {0} is not a prime number.".format(num.get()))
    

main()

