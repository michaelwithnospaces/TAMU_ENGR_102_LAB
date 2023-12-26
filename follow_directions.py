# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-1
# Date: 08 AUGUST 2023
#

import math
#function in question
def f(x):
    return math.sin(x - 1) / (x - 1)

def main():
    print("This shows the evaluation of sin(x-1)/(x-1) evaluated close to x=1")

    guess = 1.57079632679
    print(f"My guess is {guess}")

    x_values = [1.1, 1.01, 1.001, 1.0001, 1.00001, 1.000001, 1.0000001, 1.00000001]
    for i in x_values:
        result = f(i)
        print(result)

    difference = math.fabs(guess - result)
    print(f"\nMy guess was {difference} off")
#call onto main
if __name__ == "__main__":
    main()