# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-11
# Date: 19 NOVEMBER 2023

import os
def string_to_dict(user_passport):
    '''converts each string with colon seperated elements seperated by spaces into a dictionary'''
    user_passport_dict = {}
    user_passport_list = user_passport.split()
    for field in user_passport_list:
        key, value = field.split(':')
        user_passport_dict[key] = value

    return  user_passport_dict
def check_field_rules(user_passport_list):
    '''checks each field for correct rule, returns true or false based on validity of passport based off rules'''
    valid_passport_list = []

    for passport in user_passport_list:
        user_passport_dict = string_to_dict(passport)
        is_valid = True  # passport is valid until proven otherwise

        # byr – Birth year – four digits, between 1920 and 2007, inclusive
        if (len(user_passport_dict['byr']) != 4) or (int(user_passport_dict['byr']) < 1920) or (int(user_passport_dict['byr']) > 2007):
            is_valid = False

# iyr – Issue year – four digits, between 2013 and 2023, inclusive
        if (len(user_passport_dict['iyr']) != 4) or (int(user_passport_dict['iyr']) < 2013) or (int(user_passport_dict['iyr']) > 2023):
            is_valid = False

# eyr – Expiration year – four digits, between 2023 and 2033, inclusive
        if (len(user_passport_dict['eyr']) != 4) or (int(user_passport_dict['eyr']) < 2023) or (int(user_passport_dict['eyr']) > 2033):
            is_valid = False

# hgt – Height – a number followed by either cm or in
        # If cm, the number must be between 150 and 193, inclusive
        # If in, the number must be between 59 and 76, inclusive
        if 'in' not in user_passport_dict['hgt'] and 'cm' not in user_passport_dict['hgt']:
            is_valid = False
        elif 'in' in user_passport_dict['hgt']:
            int_inch = int(user_passport_dict['hgt'][0:-2])
            if int_inch < 59 or int_inch > 76:
                is_valid = False
        else:
            int_cm = int(user_passport_dict['hgt'][0:-2])
            if int_cm < 150 or int_cm > 193:
                is_valid = False

# hcl – Hair color – a # followed by exactly 6 characters (0-9 or a-f)
        if '#' not in user_passport_dict['hcl']:
            is_valid = False
        else:
            string_to_check = user_passport_dict['hcl'][1:-1]
            for letter in string_to_check:
                allowed_char = ['0', '1', '2', '3','4','5','6','7','8','9','a','b','c','d','e','f']
                if letter not in allowed_char:
                    is_valid = False
                    break

# pid – Passport ID – a nine-digit number, including leading zeroes
        if len(user_passport_dict['pid']) != 9:
            is_valid = False

# cid – Country ID – a three-digit number, NOT including leading zeroes
        if int(user_passport_dict['cid']) < 100:
            is_valid = False

        if is_valid:
            valid_passport_list.append(passport)

    return valid_passport_list
def check_passport_fields(user_passport_list):
    '''removes passports with missing fields'''

    # list declaring required fields
    required_passport_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'pid:', 'cid:']
    valid_passports = []  # declare empty valid passports list

    for passport in user_passport_list:  # iterates through each passport in list
        is_valid = True  # passport is valid until proven otherwise

        for field in required_passport_fields:  # iterates through each required field
            if field not in passport:  # if said field is missing, passport not valid
                is_valid = False
                break  # break if one field missing, no need to check for others

        if is_valid:
            valid_passports.append(passport)

    return valid_passports
def main():
    user_file_name = input('Enter the name of the file: ')

    # user_file_name = 'scanned_passports.txt'  # Hard coded user_file_name

    # open file to read and splits up by new empty line
    with open(user_file_name, 'r') as file:
        indented_passport_list = file.read().split('\n\n')

    valid_fields_passport_list  = check_passport_fields(indented_passport_list)

    valid_rules_passport_list = check_field_rules(valid_fields_passport_list)

    # writes filtered passport list to new file
    with open('valid_passports2.txt', 'w') as new_file:
        for passport in valid_rules_passport_list:
            new_file.write(passport + '\n\n')

    print(f'There are {len(valid_rules_passport_list)} valid passports')

if __name__ == "__main__":
    main()