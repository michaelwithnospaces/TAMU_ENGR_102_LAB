# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-4
# Date: 02 OCTOBER 2023
#

import math

amount_payed = float(input("How much did you pay? "))
amount_cost = float(input("How much did it cost? "))

# Calculate change in cents (as an integer)
change_in_cents = float((amount_payed - amount_cost) * 100)

# Prevent less than 1 rounding error
change_in_cents = math.ceil(change_in_cents) if (change_in_cents <= 1) else change_in_cents

print(f'You received ${change_in_cents / 100:.2f} in change. That is...')

# Quarters calculation
if change_in_cents >= 25:
    num_quarters = change_in_cents // 25
    print(f'{int(num_quarters)} {"quarters" if num_quarters > 1 else "quarter"}')
    change_in_cents -= num_quarters * 25

if change_in_cents >= 10:
    num_dimes = change_in_cents // 10
    print(f'{int(num_dimes)} {"dimes" if num_dimes > 1 else "dime"}')
    change_in_cents -= num_dimes * 10

if change_in_cents >= 5:
    num_nickels = change_in_cents // 5
    print(f'{int(num_nickels)} {"nickels" if num_nickels > 1 else "nickel"}')
    change_in_cents -= num_nickels * 5

if change_in_cents >= 1:
    num_pennies = change_in_cents
    print(f'{int(num_pennies)} {"pennies" if num_pennies > 1 else "penny"}')
