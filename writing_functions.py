# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-2
# Date: 15 SEPTEMBER 2023

import math
# math import

def area_triangle(side):
    area = (math.sqrt(3) / 4) * (side ** 2)
    return area


def area_square(side):
    area = side ** 2
    return area


def area_pentagon(side):
    area = 1/4 * (math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2)
    return area


def area_dodecagon(side):
    area = 3 * (2 + math.sqrt(3)) * side ** 2
    return area


def main():
    side = float(input('Please enter the side length: '))
    print(f'A triangle with side {side:.2f} has area {area_triangle(side):.3f}')
    print(f'A square with side {side:.2f} has area {area_square(side):.3f}')
    print(f'A pentagon with side {side:.2f} has area {area_pentagon(side):.3f}')
    print(f'A dodecagon with side {side:.2f} has area {area_dodecagon(side):.3f}')


if __name__ == "__main__":
    main()
