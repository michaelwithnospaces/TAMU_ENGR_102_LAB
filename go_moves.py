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

# collects row or column
def collectRowOrColumn(go_board_list, row_or_column):
    # define valid inputs
    valid_inputs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'g']

    print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
    position = input()
    print()

    # checks for valid inputs
    while position not in valid_inputs:
        print('Error: Invalid input')
        print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ',end='')
        position = input()
        print()

    # check for g for instructions
    while position == 'g':
        printInstructions(go_board_list)
        print()
        print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ',end='')
        position = input()
        print()
        while position not in valid_inputs:
            print('Error: Invalid input')
            print(f'Pick a {row_or_column}: then [enter] or "g" for instruction grid\n> ', end='')
            position = input()
            print()

    return int(position)

# instructions grid printing
def printInstructions(go_board_list):
    for instruction_row in range(len(go_board_list)):
        for j in range(9):
            print(f'{instruction_row}-{j}',end='  ')
        print()

# collection position for desired player
def collectPosition(go_board_list, used_positions_list, player_name):

    print(f'Player {player_name} turn. (If you would like to see the instruction grid, type "g")', end='\n\n')

    row = collectRowOrColumn(go_board_list, 'row')
    column = collectRowOrColumn(go_board_list, 'column')
    new_pair = (row, column)

    # this is to confirm the pair entered is not already used.
    while new_pair in used_positions_list:
        print(f'The pair: {new_pair} has already been placed. Please enter another pair',end='\n\n')
        row = collectRowOrColumn(go_board_list, 'row')
        column = collectRowOrColumn(go_board_list, 'column')
        new_pair = (row, column)

    return new_pair

# printing default empty board
def goBoardPrint(go_board_list):
    for row,row_list in enumerate(go_board_list):
        for column in range(len(row_list)):
            if len(go_board_list[row][column]) == 0:
                print('.', end='')
            else:
                print(go_board_list[row][column], end='')
        print()

def main():
    # initialize empty go board
    go_board = [[], [], [], [], [], [], [], [], []]

    #list of used positions
    used_positions = []

    # fill go board with periods
    for row in range(len(go_board)):
        for i in range(9):
            go_board[row].append(str('.'))

    print('Welcome to go-board!\n')

    # collect player names
    player_one = input(f'Please enter the name of player one (white {chr(9679)}): \n> ').strip()
    print()
    while len(player_one) > 12:
        print('Error: Exceeds 12 characters. Please input a valid name')
        player_one = input(f'Please enter the name of player one (white {chr(9679)}): \n> ').strip()
        print()

    player_two = input(f'Please enter the name of player two (black {chr(9675)}): \n> ').strip()
    print()
    while len(player_two) > 12:
        print('Error: Exceeds 12 characters. Please input a valid name')
        player_two = input(f'Please enter the name of player one (white {chr(9679)}): \n> ').strip()
        print()

    print (f'Welcome {player_one} and {player_two}!')
    print(f'Place your rock by providing the row then the column. Here is how they are numberd:\n')

# prints number grid
    printInstructions(go_board)

    print()

    # this is the main game loop
    while not (len(used_positions) > 81):

        # player one
        new_pair_one = collectPosition(go_board, used_positions, player_one)
        # append new pair to existing pairs
        used_positions.append(new_pair_one)

        go_board[ new_pair_one[0] ][new_pair_one[1]] = f'{chr(9679)}'
        goBoardPrint(go_board)
        print('\n')

        # player two
        new_pair_two = collectPosition(go_board, used_positions, player_two)
        # append new pair to existing pairs
        used_positions.append(new_pair_two)

        go_board[new_pair_two[0]][new_pair_two[1]] = f'{chr(9675)}'
        goBoardPrint(go_board)
        print('\n')
if __name__ == "__main__":
    main()