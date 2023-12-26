# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-2
# Date: 15 SEPTEMBER 2023

import math

tau = math.pi * 2

rounding_precision = int(input('Please enter the number of digits of precision for tau: '))

print(f'The value of tau to {rounding_precision} digits is: {tau:.{rounding_precision}f}')
