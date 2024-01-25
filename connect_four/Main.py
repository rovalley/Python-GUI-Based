'''
NAME
    Main

DESCRIPTION
    This module provides a class to play a game of connect four

Created on January 22, 2024

@author: Ryan O'Valley
'''

from tkinter import *

from GameBoard import GameBoard

# method to test checking for connect four
def test():
    game_board = GameBoard()

    game_board.drop("R",1)
    game_board.drop("R", 1)
    game_board.drop("R", 1)
    game_board.drop("R", 1)
    game_board.drop("R",2)
    game_board.drop("R", 2)
    game_board.drop("R", 2)
    game_board.drop("R", 3)
    game_board.drop("R", 3)
    game_board.drop("R", 4)

    game_board.display_board()
    print(game_board.check_for_four_dia("R"))

# method to play a game of connect four
def play_game():
    # create game board
    game_board = GameBoard()
    # create tk
    root = Tk()
    # set tk title
    root.title("Connect Four")
    # create blue label
    blue_label = Label(root, text="blue: ")
    # create red label
    red_label = Label(root, text="red: ")
    # add blue label to grid
    blue_label.grid(row=0, column=0)
    # add red label to grid
    red_label.grid(row=1, column=0)
    # create blue score label
    blue_score = Label(root, text=game_board.blue_score)
    # create red score label
    red_score = Label(root, text=game_board.red_score)
    # add blue score label to grid
    blue_score.grid(row=0, column=1)
    # add red score label to grid
    red_score.grid(row=1, column=1)
    # create current turn label
    current_turn = Label(root, text=game_board.get_current_turn())
    # add current turn label to grid
    current_turn.grid(row=0, column=3)
    # create winner label
    winner_label = Label(root, text="")
    # add winner label to grid
    winner_label.grid(row=1, column=2, columnspan=3)
    # create tokens dictionary
    tokens = {}
    # loop through rows
    for row_num in range(6):
        tokens[row_num] = {}
        # loop through column numbers
        for col_num in range(7):
            tokens[row_num][col_num] = Label(root, text=" ")
            tokens[row_num][col_num].grid(row=row_num + 4, column=col_num)
    # create play again button
    play_again = Button(root, text="Play Again", command=lambda: start_new_game(game_board, winner_label, tokens, root))
    # add play again button to grid
    play_again.grid(row=0, column=5, columnspan=2)
    # create labels dictionary
    labels = {}
    # add current turn label to labels dictionary
    labels["current_turn"] = current_turn
    # add blue score label to labels dictionary
    labels["blue_score"] = blue_score
    # add red score label to labels dictionary
    labels["red_score"] = red_score
    # add winner label to labels dictionary
    labels["winner_label"] = winner_label

    # add action to the drop buttons
    drop_0 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 0))
    drop_0.grid(row=3, column=0)
    drop_1 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 1))
    drop_1.grid(row=3, column=1)
    drop_2 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 2))
    drop_2.grid(row=3, column=2)
    drop_3 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 3))
    drop_3.grid(row=3, column=3)
    drop_4 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 4))
    drop_4.grid(row=3, column=4)
    drop_5 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 5))
    drop_5.grid(row=3, column=5)
    drop_6 = Button(root, text="drop", command=lambda: drop(tokens, labels, game_board, 6))
    drop_6.grid(row=3, column=6)


    root.mainloop()

# method to drop
def drop(tokens, labels, game_board, col_num):
    # set successful drop
    successful_drop = game_board.drop(col_num)
    # if successful drop
    if successful_drop:
        # display game board
        display_board(tokens, game_board)
        # set winner
        winner = game_board.check_winner()
        # if there is no winner
        if winner is None:
            # switch turns
            game_board.switch_turns()
            # set current turn label
            labels["current_turn"]["text"] = game_board.get_current_turn()
            # if game board is full with tokens
            if game_board.is_board_full():
                # display tie
                labels["winner_label"]["text"] = "tie"
        else:
            # set red score label
            labels["red_score"]["text"] = game_board.red_score
            # set blue score label
            labels["blue_score"]["text"] = game_board.blue_score
            # if winner is red
            if winner == "r":
                # display red has won
                labels["winner_label"]["text"] = "Red has won"
            # if winner is blue
            elif winner == "b":
                # display blue has won
                labels["winner_label"]["text"] = "Blue has won"

# method to display board
def display_board(tokens, game_board):
    # loop through rows in tokens
    for row_num in range(len(tokens)):
        # loop through columns in tokens
        for col_num in range(len(tokens[row_num])):
            # set color
            color = game_board.get_color(row_num, col_num)
            # set token
            tokens[row_num][col_num]['text'] = " "
            # if color is b
            if color == "b":
                # set token background color to blue
                tokens[row_num][col_num]["bg"] = "blue"
            # if color is r
            elif color == "r":
                # set token background color to red
                tokens[row_num][col_num]["bg"] = "red"
            else:
                tokens[row_num][col_num]['text'] = ""

# method to start a new game
def start_new_game(game_board, winner_label, tokens, root):\
    # create new game board
    game_board.new_game()
    winner_label["text"] = ""
    # display game board
    display_board(tokens, game_board)
    # loop through rows in tokens
    for row_num in tokens:
        #loop through columns in tokens
        for col_num in tokens[row_num]:
            tokens[row_num][col_num] = Label(root, text=" ")
            tokens[row_num][col_num].grid(row=row_num + 4, column=col_num)

if __name__ == '__main__':
    play_game()
