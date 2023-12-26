# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-6
# Date: 28 SEPTEMBER 2023

import math
def pyramid_area(side, layers):
    # visible top surface area calculations
    top_side_area = (math.sqrt(3) / 4) * (side ** 2)  # area of top side (equilateral triangle)
    visible_top_area = 0
    for i in range(1, layers + 1):
        # takes current prism count and subtracts previous layer prism count
        visible_top_area += top_side_area * (i ** 2) - (((i - 1) ** 2) * top_side_area)

    # visible sides of each layer calculations
    visible_side_count = 0
    side_area = side ** 2  # area of side (square)
    for j in range(1, layers + 1):
        visible_side_count += j * 3
    visible_side_area = visible_side_count * side_area

    total_area = visible_side_area + visible_top_area

    print(f'You need {total_area:.2f} m^2 of gold foil to cover the pyramid')

def main():
    length_of_side = float(input("Enter the side length in meters: "))
    number_of_layers = int(input("Enter the number of layers: "))
    pyramid_area(length_of_side, number_of_layers)

if __name__ == "__main__":
    main()