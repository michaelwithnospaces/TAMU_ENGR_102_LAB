# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB_7
# Date: 24 OCTOBER 2023

# less than 10 days calculation
def numGadgetsTenLess(number_of_days):
    number_of_gadgets = 10 * number_of_days
    return number_of_gadgets

# less than 50 days calculation
def numGadgetsFiftyLess(number_of_days):
    number_of_gadgets = 0
    number_of_gadgets += 10 * number_of_days  # adds constant 100 per day
    number_of_gadgets += (number_of_days * (number_of_days + 1)) / 2  # triangular number infite series, add 50 excess
    return number_of_gadgets

def numGadgetsMaxSpeed(number_of_days):
    number_of_gadgets = 50 * number_of_days
    return number_of_gadgets

def main():
    user_days = int(input('Please enter a positive value for day: '))

    # checks for valid input
    if user_days < 0:
        print('You entered an invalid number!')
        exit()

    # initialize number of gadgets
    number_of_gadgets = 0

    # less than 10 days of producion
    if user_days <= 10:
        number_of_gadgets += numGadgetsTenLess(user_days)

    # less than 50 days of production
    elif user_days <= 50:
        number_of_gadgets += numGadgetsTenLess(10)  # first 10 days
        number_of_gadgets += numGadgetsFiftyLess(user_days - 10)

    elif user_days < 101:
        number_of_gadgets += numGadgetsTenLess(10)  # first 10 days
        number_of_gadgets += numGadgetsFiftyLess(40) # next 40 days
        number_of_gadgets += numGadgetsMaxSpeed(user_days - 50)

    else:
        number_of_gadgets += numGadgetsTenLess(10)  # first 10 days
        number_of_gadgets += numGadgetsFiftyLess(40)  # next 40 days
        number_of_gadgets += numGadgetsMaxSpeed(50)

    print(f'The sum total number of gadgets produced on day {user_days} is {number_of_gadgets:.0f}')

if __name__ == "__main__":
    main()