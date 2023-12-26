# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: MICHAEL NGUYEN
# Section: 536
# Assignment: LAB_7
# Date: 24 OCTOBER 2023

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# Converts words to pig latin
def convertPigLatin(word, position):
    if position == 0:
        converted_word = f'{word}yay'
    else:
        converted_word = f'{word[position:]}{word[:position]}ay'
    return converted_word
def main():
    converted_user_input = []
    user_input = input('Enter word(s) to convert to Pig Latin: ').strip().lower()
    user_input_list = user_input.split()

    for word in user_input_list:
        for letter in word:
            if letter in vowels:   # Checks if vowel exists
                word_pos = word.find(letter)   # Finds position of first vowel
                converted_user_input.append(convertPigLatin(word, word_pos))
                break

    print(f'In Pig Latin, "{user_input}" is:', end = " ")
    for i in range(len(converted_user_input)):
        print(converted_user_input[i], end= ' ')
if __name__ == "__main__":
    main()