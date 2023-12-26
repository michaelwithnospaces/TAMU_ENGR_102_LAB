# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: MICHAEL NGUYEN
# NAME OF TEAM MEMBER 2
# NAME OF TEAM MEMBER 3
# NAME OF TEAM MEMBER 4
# Section: 536
# Assignment: LAB-8
# Date: 26 OCTOBER 2023

def convertToStandard(user_input):

    user_time_list = user_input.split(':')
    raw_hour = int(user_time_list[0])
    if raw_hour == 0:
        new_hour = 12
        converted_time = f'{new_hour}:{user_time_list[1]}'
        return converted_time

    elif raw_hour > 12:
        if raw_hour == 13:
            new_hour = 1
        if raw_hour == 14:
            new_hour = 2
        if raw_hour == 15:
            new_hour = 3
        if raw_hour == 16:
            new_hour = 4
        if raw_hour == 17:
            new_hour = 5
        if raw_hour == 18:
            new_hour = 6
        if raw_hour == 19:
            new_hour = 7
        if raw_hour == 20:
            new_hour = 8
        if raw_hour == 21:
            new_hour = 9
        if raw_hour == 22:
            new_hour = 10
        if raw_hour == 23:
            new_hour = 11
        if raw_hour == 24:
            new_hour = 12

        converted_time = f'{new_hour}:{user_time_list[1]}'
        return converted_time

    else:
        return user_input

def numberCheck(digit, c, default):

    if not default:
        if digit == '0':
            return  timeZero(c)
        if digit == '1':
            return timeOne(c)
        if digit == '2':
            return timeTwo(c)
        if digit == '3':
            return timeThree(c)
        if digit == '4':
            return timeFour(c)
        if digit == '5':
            return timeFive(c)
        if digit == '6':
            return timeSix(c)
        if digit == '7':
            return timeSeven(c)
        if digit == '8':
            return timeEight(c)
        if digit == '9':
            return  timeNine(c)
    else:
        if digit == '0':
            return timeZero()
        if digit == '1':
            return timeOne()
        if digit == '2':
            return timeTwo()
        if digit == '3':
            return timeThree()
        if digit == '4':
            return timeFour()
        if digit == '5':
            return timeFive()
        if digit == '6':
            return timeSix()
        if digit == '7':
            return timeSeven()
        if digit == '8':
            return timeEight()
        if digit == '9':
            return timeNine()

def timeOne(c = '1'):
    timeOne = [f' {c} ',f'{c}{c} ', f' {c} ' , f' {c} ',f'{c}{c}{c}']
    return  timeOne
def timeTwo(c = '2'):
    timeTwo = [f'{c}{c}{c}', f'  {c}', f'{c}{c}{c}', f'{c}  ', f'{c}{c}{c}']
    return  timeTwo
def timeThree(c = '3'):
    timeThree = [f'{c}{c}{c}',f'  {c}', f'{c}{c}{c}', f'  {c}', f'{c}{c}{c}']
    return timeThree
def timeFour(c = '4'):
    timeFour = [f'{c} {c}', f'{c} {c}',f'{c}{c}{c}', f'  {c}', f'  {c}']
    return timeFour
def timeFive(c = '5'):
    timeFive = [f'{c}{c}{c}', f'{c}  ' , f'{c}{c}{c}', f'  {c}', f'{c}{c}{c}']
    return timeFive
def timeSix(c = '6'):
    timeSix = [f'{c}{c}{c}', f'{c}  ', f'{c}{c}{c}', f'{c} {c}', f'{c}{c}{c}']
    return timeSix
def timeSeven(c = '7'):
    timeSeven = [f'{c}{c}{c}', f'  {c}', f'  {c}', f'  {c}', f'  {c}' ]
    return timeSeven
def timeEight(c = '8'):
    timeEight = [f'{c}{c}{c}', f'{c} {c}', f'{c}{c}{c}', f'{c} {c}', f'{c}{c}{c}']
    return timeEight
def timeNine(c = '9'):
    timeNine = [f'{c}{c}{c}', f'{c} {c}', f'{c}{c}{c}', f'  {c}', f'{c}{c}{c}']
    return timeNine
def timeZero(c = '0'):
    timeZero = [f'{c}{c}{c}',f'{c} {c}',f'{c} {c}',f'{c} {c}',f'{c}{c}{c}']
    return  timeZero
def printAscii(time_list, column):
    for i in range(5):
        for j in range(column):
            if j != (column -1):
                print(time_list[j][i],end = ' ')
            else:
                print(time_list[j][i], end='')
        print()
def main():

    # list of allowed characters for numbers
    allowed_char = ["$", "@", '*']

    # collect user input
    user_input = input('Enter the time: ')
    user_time_type = int(input('Choose the clock type (12 or 24): '))
    c = input('Enter your preferred character: ').strip()
    while  (c != '')  and (c not in allowed_char):
        c = input('Character not permitted! Try again: ')

    print()

    # check/conversion to standard hour
    if user_time_type == 24:
        user_time = str(user_input)
    elif user_time_type == 12:
        user_time = str(convertToStandard(user_input))

    # converted integer list
    user_time_list = user_time.split(':')
    raw_hour = int(user_time_list[0])
    raw_minute = int(user_time_list[1])

    # original user input integer list
    og_user_time_list = user_input.split(':')
    og_raw_hour = int(og_user_time_list[0])
    og_raw_minute = int(og_user_time_list[1])

    # single or double digit hour determination
    if raw_hour < 10:
        time_positions = [[], [' ', ':', ' ', ':', ' '], [], [], [],
                            ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M']]
        military_time_positions = [[], [' ', ':', ' ', ':', ' '], [], []]
    else:
            time_positions = [[], [], [' ', ':', ' ', ':', ' '], [], [], [],
                              ['M   M', 'MM MM', 'M M M', 'M   M', 'M   M']]
            military_time_positions = [[], [], [' ', ':', ' ', ':', ' '], [], []]



    # determine if use default characted or custom character input
    if c in allowed_char:
        use_default = False
    else:
        use_default = True

    # standard time
    if user_time_type == 12:

        time_positions[0] = numberCheck(user_time[0], c, use_default)
        if raw_hour >= 10:  # only if double digit hour
            time_positions[1] = numberCheck(user_time[1], c, use_default)
        time_positions[-4] = numberCheck(user_time[-2], c, use_default)
        time_positions[-3] = numberCheck(user_time[-1], c, use_default)
        if og_raw_hour < 12:
            time_positions[-2]  = [' A ', 'A A', 'AAA', 'A A', 'A A']
        else:
            time_positions[-2] = ['PPP', 'P P', 'PPP', 'P  ', 'P  ']

        printAscii(time_positions, len(time_positions))

# military time
    elif user_time_type == 24:
        military_time_positions[0] = numberCheck(user_time[0], c, use_default)
        if raw_hour >= 10:  # only if double digit hour
            military_time_positions[1] = numberCheck(user_time[1], c, use_default)
        military_time_positions[-2] = numberCheck(user_time[-2], c, use_default)
        military_time_positions[-1] = numberCheck(user_time[-1], c, use_default)

        printAscii(military_time_positions,len(military_time_positions))

    else:
        print('Please enter a valid time type')
        exit()


if __name__== "__main__":
    main()