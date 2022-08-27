import math
from operator import truediv

# Geometry solver class
# Collection of methods for calculating various geometric formulas.


class geometry_calculator(object):
    @staticmethod
    def area_of_circle(radius):
        ans = math.pi * radius**2
        return (ans)

    @staticmethod
    def area_of_rect(width, length):
        ans = width*length
        return (ans)

    @staticmethod
    def volume_of_box(width, length, depth):
        area = width*length
        vol = area+depth
        return (vol)

    # consider adding more volume methods

    @staticmethod
    def volume_of_sphere(radius):
        ans = (4/3) * (math.pi*radius**3)
        return (ans)

# main function
# entry point for the program
# prints a simple menu- you make the choice and supply the values


def main():
    running = True

    while (running):
        print_menu()

        # user selects an option.
        choice = input('Your choice? ')
        if choice == "X" or choice == "x":
            print('Thank you for playing... Goodbye!')
            running = False
        elif choice == "1":
            response = input('Radius? ')
            r = float(response)
            ans = geometry_calculator.area_of_circle(r)
            print(f'Area of circle with a radius {r} is {ans}.')
        elif choice == "2":
            response = input('Width? ')
            w = float(response)
            response = input('Length? ')
            l = float(response)
            ans = geometry_calculator.area_of_rect(w, l)
            print(f'Area of rectangle with width {w} and height {l} is {ans}.')
        elif choice == "3":
            response = input('Width? ')
            w = float(response)
            response = input('Length? ')
            l = float(response)
            response = input('Depth? ')
            d = float(response)
            ans = geometry_calculator.volume_of_box(w, l, d)
            print(
                f'Volume of rectangle with width {w}, height {l}, and depth {d} is {ans}.')
        elif choice == "4":
            response = input('Radius? ')
            r = float(response)
            ans = geometry_calculator.volume_of_sphere(r)
            print(f'Volume of a sphere with radius {r} is {ans}.')


def print_menu():
    # print the menu
    print()  # blank line
    print('Welcome to the Geometry Solver!')
    print('-------------------------------')
    print('1. Area of a circle')
    print('2. Area of a rectangle')
    print('3. Volume of a box')
    print('4. Volume of a sphere')
    print('X. Exit')
    print()  # blank line


    # If we're running this module as the main program, execute main()
if __name__ == "__main__":
    main()
