# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-2
# Date: 07 SEPTEMBER 2023

import math

x1 = 10
x2 = 55
y1 = 2027
y2 = 23027
radius = 6745

circumference = 2 * math.pi * radius
slope = (y2 - y1) / (x2 - x1)

x = 25

p1 = slope * (x - x1) + y1
p1 = p1 % circumference

print('Part 1:')
print(f'For t = 25 minutes, the position p = {p1} kilometers')

#recalculation for part 2
x = 300
p2 = slope * (x - x1) + y1
p2 = p2 % circumference

print('Part 2:')
print(f'For t = 300 minutes, the position p = {p2} kilometers')