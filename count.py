import math

def isPrime(number):
    if number < 2: # all numbers less than 2 are not prime
        return False

    # for i in range(2, number): Loop through numbers from 2 to but not including the current number
    for i in range(2, int(math.sqrt(number)) + 1): # Loop through numbers from 2 to square root of the current number
        if number % i == 0: # if the number has any divisors other than 1 and itself, it is not prime
            return False
    return True # if no divisors are found, the current number is prime

# Function to display prime numbers and write them to a file
def displayPrimeNumbers():
    with open("results.txt", "w") as file:
        for number in range(1, 251):
            if isPrime(number):
                file.write(f"{number} ") # if a number is prime, write to the file, separated by space

displayPrimeNumbers() 
print("Check results.txt")

with open("results.txt", "r") as file:
    print(file.read()) # print a content in a terminal to check if the function works correct
    