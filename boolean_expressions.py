# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-4
# Date: 03 OCTOBER 2023

############ Part A ############

expression = input(f'Enter True or False for a: ').strip().upper()
bool_expression = expression[0]
a = bool_expression == 'T'

expression = input(f'Enter True or False for b: ').strip().upper()
bool_expression = expression[0]
b = bool_expression == 'T'

expression = input(f'Enter True or False for c: ').strip().upper()
bool_expression = expression[0]
c = bool_expression == 'T'

############ Part B ############

# And print statement
and_statement = a and b and c
print(f'a and b and c: {and_statement}')

# Or print statement
or_statement = a or b or c
print(f'a or b or c: {or_statement}')

############ Part C ############

# XOR print statement
xor_statement = ((a == True) and (b == False)) or ((a == False) and (b == True))
print(f'XOR: {xor_statement}')

# Odd print statement
odd_statement = ((a and not (b or c)) or (b and not (a or c)) or (c and not (a or b))) or (a and b and c)
print(f'Odd number: {odd_statement}')

############ Part D ############

complex_1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
print(f'Complex 1: {complex_1}')

complex_2 = ((not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and
             (not a or (a and b and c) or (a and ((b and not c) or (not b)))))
print(f'Complex 2: {complex_2}')

simple_1 = not b or not a and not c
print(f'Simple 1: {simple_1}')