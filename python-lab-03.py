# Code: Miles Per Gallon Program
# Author: Lance Howell
# Class: ISYS-674: Network Security 
# Description: Calculates the miles per gallon and the gallons. 

print()
print('       The Miles Per Gallon Program')
print()

milesDriven=int(input('       Enter miles driven:  '))  # I use the input statement to gather the miles driven from the user then convert that string value into an integer. 
gallonsGas=float(input('Enter gallons of gas used:  ')) # I use the input statement to gather the gallons of gas used from the user and then convert that string value into a float.

print('                            _______')
print()

MilesGallon=milesDriven/gallonsGas  # This calculates the Miles per Gallon rounding the number to the nearest 100th. 

print(f'         Miles Per Gallon:  {MilesGallon:.2f}' ) # This statement prints out the calculation to the screen. 
print('Bye')
print()