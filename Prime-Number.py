# Sample Program: Prime Number Program
# Programming 1: Python Introduction
# Author: Lance Howell
# Description: Discover prime numbers by using statement control statements. 

n=0 # Initialize number variable.
prime = True # Start by assuming it is prime

n = int(input('Enter a number: ')) # Asks the user to enter a number. Assigns the number to the variable.

if (n <= 1):  # 1 and lower are not prime
    prime = False

for factor in range (2,n):  # check all possible factors (2, n)
    if (n % factor == 0): # n%factor == 0 when it is a divisor
        prime = False # set that n is not prime

if prime: 
    print (f'{n} is a prime number') # the number is prime
else:
    print (f'{n} is not a prime number') # the number is not prime