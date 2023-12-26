# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB_9
# Date: 19 NOVEMBER 2023


def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzzle):
    unique_letters = []  # creates a empty unique letters array
    for letter in puzzle:
        if (letter in unique_letters) or not letter.isalpha():  # if letter is in unique letters or not a letter
            continue
        else:
            unique_letters.append(letter)
    unique_letters_string = ''.join(str(x) for x in unique_letters) # converts array of unique letters to string
    return unique_letters_string

def is_valid_guess(unique_letters_string, guess_string):
    unique_letter_array = [x for x in unique_letters_string]    # converts unique letter array to string
    is_valid = True  # valid guess until proven otherwise
    for letter in  guess_string:
        if letter in unique_letter_array:
            unique_letter_array.remove(letter)
        else:  # if letter not unique in unique letters array, imeddiately false, break
            is_valid = False
            break

    if len(unique_letter_array) != 0: # checks if same length
        is_valid = False

    return  is_valid

def check_user_guess(dividend, quotient, divisor, remainder):
    if dividend == quotient * divisor + remainder:
        return True
    else:
        return False

def make_number(word_to_int, user_guess):
    new_integer = []  # creates integer array

    for letter in word_to_int:
        index  = user_guess.find(letter)  # finds letter in puzzle
        new_integer.append(index)  # appends index integer to new integer array

    new_integer = ''.join(str(x) for x in new_integer)   # converts array to string
    return int(new_integer)  # returns integer

def make_numbers(puzzle_word, user_guess):

    puzzle_word = puzzle_word.replace('|', ',')
    puzzle_word = puzzle_word.replace(' ', '')
    puzzle_word = puzzle_word.replace('.', '')
    puzzle_word_array = puzzle_word.split(',')

    dividend = make_number(puzzle_word_array[2], user_guess)
    quotient = make_number(puzzle_word_array[0], user_guess)
    divisor = make_number(puzzle_word_array[1], user_guess)
    remainder = make_number(puzzle_word_array[-1], user_guess)

    new_tuple = (dividend, quotient, divisor, remainder)
    return new_tuple

def main():
    # The lines below demonstrate what the print_puzzle function outputs.

    puzzle_input = input('Enter a word arithmetic puzzle: ')
    print()
    print_puzzle(puzzle_input)
    print()

    user_input = input('Enter your guess, for example ABCDEFGHIJ: ')
    if is_valid_guess(get_valid_letters(puzzle_input), user_input) == False:
        print ('Your guess should contain exactly 10 unique letters used in the puzzle.')
    else:
        integer_tuple = make_numbers(puzzle_input, user_input)
        checked_guess = check_user_guess(integer_tuple[0],integer_tuple[1], integer_tuple[2],integer_tuple[3])

        if checked_guess == True:
            print('Good job!')
        else:
            print('Try again!')

if __name__ == '__main__':
    main()