class NaturalNumber:
    def __init__(self, n):
        self.n = n  # Store the input number as an instance variable

    def get(self):
        return self.n  # Return the stored number

    def isEven(self):
        return self.n % 2 == 0  # Check if the number is divisible by 2

    def isSquare(self):
        # Check if there exists any integer k such that k^2 equals the number
        for k in range(1, self.n):
            if self.n == k ** 2:
                return True
        return False
    
    def isPrime(self):
        prime = True  # Assume the number is prime initially
        
        # Prime numbers are greater than 1
        if self.n > 1:  
            # Check for divisibility from 2 up to n - 1
            for i in range(2, self.n):
                print("Checking for divisibility with:", i)  # Debug message
                # If self.n is divisible by any number in this range, it's not prime
                if (self.n % i) == 0: 
                    prime = False  # Found a divisor → not prime
                    break  # No need to check further
        else: 
            # If the number is 1 or less, it's not prime
            prime = False

        return prime  # Return the result of the primality check



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
