import math

# User inputs
user_integer = int(input("Enter a 4-digit integer: "))
original_integer = user_integer
user_power = int(input("Enter the power: "))

# Collect digits
thousand_place = user_integer // 1000
user_integer = user_integer % 1000
hundred_place = user_integer // 100
user_integer = user_integer % 100
ten_place = user_integer // 10
user_integer = user_integer % 10
one_place = user_integer
sum_raised_digits = (thousand_place ** user_power) + (hundred_place ** user_power) + (ten_place ** user_power) + (one_place ** user_power)


if sum_raised_digits == original_integer:
    print(f'{original_integer} with given power {user_power} is a PDI')
else:
    print(f'{original_integer} with given power {user_power} is NOT a PDI')
