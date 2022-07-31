# Challenge: Odd or Even
# Class: Programming 1: Introduction to Python
# Author: Lance Howell

# Initialize variable. 
x = 0

# Get user input 
print()
x = int(input('Enter an odd or even number: '))

# if the number user entered is even then the statement is true otherwise it is false, so it will run the 'odd' code block.
if ((x%2) == 0):
    print()
    print(f'{x} is even')
else: 
    print()
    print(f"{x} is odd")