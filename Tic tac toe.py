"""" 
projekt_2.py: druhy projekt do Engeto Online Python Akademie

author: Jakub Filip
discord: bubak#2787
"""

import os

# greeting funciton
def greetings():
    print(""""
    Welcome to Tic Tac Toe
    =============================================
    Game rules:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their marks 
    in a:
    * horizontal,
    * vertical or
    * diagonal row
    Press 1 - 9 on your keyboard
    =============================================
    Let's start the game
    """)

# dictionary for playing_field
place = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5',
         6 : '6', 7 : '7', 8 : '8', 9 : '9'}

# function for printing playing_field
def show_playing_field(place):
    playing_field = (f"|{place[1]}|{place[2]}|{place[3]}|\n"
             f"|{place[4]}|{place[5]}|{place[6]}|\n"
             f"|{place[7]}|{place[8]}|{place[9]}|\n")
    print(playing_field)

# function for player who should play
def check_turn(turn):
    if turn % 2 == 0:
        return 'O'
    else:
        return 'X'

# function for checking if player win the game
def check_for_win(place):
    # horizontal check
    if (place[1] == place[2] == place[3]) \
        or (place[4] == place[5] == place[6]) \
        or (place[7] == place[8] == place[9]):
        return True
    # vertical check
    elif (place[1] == place[4] == place[7]) \
        or (place[2] == place[5] == place[8]) \
        or (place[3] == place[6] == place[9]):
        return True
    # diagonal check
    elif (place[1] == place[5] == place[9]) \
        or (place[3] == place[5] == place[7]):
        return True
    else:
        return False

# variables
playing =  True
result = False
turn = 0
previous_turn = -1

greetings()

# playing loop
while playing:
    # reset screen, find type of os and than use the right command to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    show_playing_field(place)
    # tell player about his invalid input
    if previous_turn == turn:
        print("Please pick another spot, this spot is not on playing field or is already taken")
    previous_turn = turn
    # show the number of player who should play
    print("Player " + str((turn % 2) + 1) + " take your spot or press 'e' to exit")
    # input from player
    player_choice = input()
    if player_choice == "e":
        exit()
    # control if player choice is digit and is in place
    elif str.isdigit(player_choice) and int(player_choice) in place:
        # control if the spot is taken by other player
        if not place[int(player_choice)] in {'X', 'O'}:
            # increasing turn about 1
            turn += 1
            # player input from string to int and change number on playing field for "O" or "X"
            place[int(player_choice)] = check_turn(turn)
    # control the ending of the game a change variable playing and complete
    if check_for_win(place): 
        playing, result = False, True
    if turn > 8:
        playing = False

# print result and show playing_field
os.system('cls' if os. name == 'nt' else 'clear')
show_playing_field(place)
# show who is the winner
if result:
    if check_turn(turn) == 'X':
        print('Player 1 (X) is the winner!')
    else:
        print('Player 2 (O) is the winner!')
else:
    # Draw
    print('Draw')



    


