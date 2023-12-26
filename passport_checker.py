# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB-11
# Date: 19 NOVEMBER 2023

import os
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

    valid_indented_passport_list  = check_passport_fields(indented_passport_list)

    # writes filtered passport list to new file
    with open('valid_passports.txt', 'w') as new_file:
        for passport in valid_indented_passport_list:
            new_file.write(passport + '\n\n')

    print(f'There are {len(valid_indented_passport_list)} valid passports')

if __name__ == "__main__":
    main()