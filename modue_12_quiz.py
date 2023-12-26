# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: MODULE-12 QUIZ
# Date: 21 NOVEMBER 2023

def findKey(matrix):
    position_to_letter = {i: chr(i + ord('a')) for i in range(26)}  # maps letter to number
    key = []

    # determine letter one
    sum = 0
    for i in range(5):
        sum  += matrix[i][85]
    key.append(position_to_letter[sum])

    sum = 0
    count = 0
    # determine letter two
    for j in matrix[4]:
        sum += j
        count += 1
    average = sum / count
    key.append(position_to_letter[average])

    # determine letter three
    sum = 0
    for k in range(-5,0):
        sum += matrix[62][k]
    key.append(position_to_letter[sum])

    # determine letter four
    min = matrix[0][0]
    for l in matrix[0]:
        if l < min:
            min = l
    key.append(position_to_letter[min])

    # determine letter five
    max = matrix[29][0]
    for m in matrix[29]:
        if m > max:
            max = m
    key.append(position_to_letter[max])

    key_string = ''.join(str(x) for x in key)

    return key_string
# This function decrypts the encrypted text and returns the original text
def originalText(cipher_text, key):
    '''This function decrypts the encrypted text and returns the original text'''
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))

def main():
    with open('module12quizF23.txt', 'r') as file:
        file_integer_list = file.readlines()

    integer_matrix = []  # initialize empty matrix
    temporary_row = []  # initialize empty list for row
    integer_count = 0  # initialize integer counter

    for integer in file_integer_list:
        current_integer = int(integer.strip())
        temporary_row.append(current_integer)
        integer_count += 1

        if integer_count == 100:
            integer_count = 0  # reset integer counter
            integer_matrix.append(temporary_row)
            temporary_row = []


    phrase_to_decipher = input('Please enter the phrase to deciper: ').strip().lower()
    key_word = findKey(integer_matrix)
    key_words_phrase_length = []
    key_word_count = 0
    for phrase_count in range(len(phrase_to_decipher)):
        key_words_phrase_length.append(key_word[key_word_count])
        key_word_count += 1
        if key_word_count == len(key_word):
            key_word_count = 0

    key_word_phrase = ''.join(str(x) for x in key_words_phrase_length)
    print(f'keyword: {key_word}')
    print(f'plain text: {originalText(phrase_to_decipher, key_word_phrase).lower()}')

if __name__ == "__main__":
    main()