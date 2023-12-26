# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-12
# Date: 21 NOVEMBER 2023

# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

a = np.arange(0,12).reshape(3,4)
b = np.arange(0,8).reshape(4,2)
c = np.arange(0,6).reshape(2,3)
print(f'A = {a}')
print()  # newline
print(f'B = {b}')
print()  # newline
print(f'C = {c}')
print()  # newline

d = a @ b @ c

print(f'D = {d}')
print()  # newline
print(f'D^T = {d.T}')
print()  # newline

e = np.sqrt(d) / 2

print(f'E = {e}')
