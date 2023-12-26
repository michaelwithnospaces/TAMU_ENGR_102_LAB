# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-3
# Date: 15 SEPTEMBER 2023

def pounds_convert(number):
    number = number * 4.44822
    return number
def meters_convert(number):
    number = number * 3.28084
    return number
def atmospheres_convert(number):
    number  = number * 101.325
    return number
def watts_convert(number):
    number = number * 3.412142
    return number
def liters_convert(number):
    number = number * 15.8503288
    return number
def celsius_convert(number):
    number = number*1.8 + 32
    return number
def main():
    #collect user input
    user_input = float(input('Please enter the quantity to be converted: '))

    #calling conversion functions
    print(f'{user_input:.2f} pounds force is equivalent to {pounds_convert(user_input):.2f} Newtons')
    print(f'{user_input:.2f} meters is equivalent to {meters_convert(user_input):.2f} feet')
    print(f'{user_input:.2f} atmospheres is equivalent to {atmospheres_convert(user_input):.2f} kilopascals')
    print(f'{user_input:.2f} watts is equivalent to {watts_convert(user_input):.2f} BTU per hour')
    print(f'{user_input:.2f} liters per second is equivalent to {liters_convert(user_input):.2f} US gallons per minute')
    print(f'{user_input:.2f} degrees Celsius is equivalent to {celsius_convert(user_input):.2f} degrees Fahrenheit')
if __name__ == "__main__":
    main()