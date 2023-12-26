# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB_4
# Date: 29 OCTOBER 2023

# initialize largest variable

largest_num = float(input('Enter number 1: ').strip())

for i in range(2,4):
    print(f'Enter number {i}:', end=' ')
    user_number = float(input().strip())

    if user_number > largest_num:
        largest_num = user_number

print(f'The largest number is {largest_num:.1f}')