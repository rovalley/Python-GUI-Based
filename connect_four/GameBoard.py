'''
NAME
    GameBoard

DESCRIPTION
    This module provides a class to create a connect four board and provides methods to play

Created on January 22, 2024

@author: Ryan O'Valley
'''

# constructor
class GameBoard:
    def __init__(self):
        self.blue_score = 0
        self.red_score = 0
        self.new_game()
        self.turn = "b"

    # method to create new game
    def new_game(self):
        # game board
        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]
        # set game over to false
        self.game_over = False

    # method to get color
    def get_color(self, row_num, col_num):
        # return the row and column
        return self.board[row_num][col_num]
    # method to drop a token
    def drop(self, col_num):
        # check if game is over
        if self.game_over:
            return False
        # set last empty to -1
        last_empty = -1
        # loop through the rows on the game board
        for row_num in range(len(self.board)):
            # check if the spot on game board is empty
            if self.board[row_num][col_num] == " ":
                # set last empty to the row number
                last_empty = row_num
        # if last empty is greater than -1
        if last_empty > -1:
            # set to turn
            self.board[last_empty][col_num] = self.turn
            return True
        else:
            return False

    # method to switch turns
    def switch_turns(self):
        # if it is blues turn
        if self.turn == "b":
            # set turn to red
            self.turn = "r"
        else:
            # set turn to blue
            self.turn = "b"

    # method to get current turn
    def get_current_turn(self):
        # if it is blues turn
        if self.turn == "b":
            # return blue
            return "blue"
        else:
            # return red
            return "red"

    # method to check if there is a winner
    def check_winner(self):
        # check if blue won
        if self.check_for_four_hor("b") or self.check_for_four_ver("b") or self.check_for_four_dia("b"):
            # increment blues score
            self.blue_score += 1
            # set game over to true
            self.game_over = True
            return "b"
        # check if red won
        elif self.check_for_four_hor("r") or self.check_for_four_ver("r") or self.check_for_four_dia("r"):
            # increment reds score
            self.red_score += 1
            # set game over to true
            self.game_over = True
            return "r"
        # no winner
        else:
            return None

    # method to display board
    def display_board(self):
        # loop through the game board rows
        for row in range(len(self.board)):
            # loop through the game board columns
            for col in range(len(self.board[row])):
                # if the spot is empty
                if self.board[row][col] == " ":
                    # print x in the empty spots
                    print("X", end="")
                else:
                    # print empty string
                    print(self.board[row][col], end="")
            print()

    # method to check if game board is full
    def is_board_full(self):
        # loop through rows on game board
        for row in range(len(self.board)):
            # loop through columns on game board
            for col in range(len(self.board[row])):
                # if game board spot is empty
                if self.board[row][col] == " ":
                    return False
        return True

    # method to check if game board column is full
    def is_full(self, col_num):
        # check if the top spot on the game board is empty
        if self.board[0][col_num] == " ":
            return False
        else:
            return True

    # method to check if there is 4 in a row horizontally
    def check_for_four_hor(self, color):
        # loop through the rows on the game board
        for row_num in range(len(self.board)):
            # loop through the columns on the game board
            for col_num in range(len(self.board[row_num]) - 3):
                # checks horizontal
                if self.board[row_num][col_num] == color and self.board[row_num][col_num] == self.board[row_num][col_num + 1]  and self.board[row_num][col_num] == self.board[row_num][col_num + 2] and self.board[row_num][col_num] == self.board[row_num][col_num + 3]:
                    return True
        return False

    # method to check if there is 4 in a row vertically
    def check_for_four_ver(self, color):
        # loop through the rows on the game board
        for row_num in range(len(self.board) - 3):
            # loop through the columns on the game board
            for col_num in range(len(self.board[row_num])):
                # checks vertical
                if self.board[row_num][col_num] == color and self.board[row_num][col_num] == self.board[row_num + 1][col_num] and self.board[row_num][col_num] == self.board[row_num + 2][col_num] and self.board[row_num][col_num] == self.board[row_num + 3][col_num]:
                    return True
        return False

    # method to check if there is 4 in a row diagonally
    def check_for_four_dia(self, color):
        # loop through the rows on the game board
        for row_num in range(len(self.board) - 3):
            # loop through the columns on the game board
            for col_num in range(len(self.board[row_num]) - 3):
                # checks diagonal top left to bottom right
                if self.board[row_num][col_num] == color and self.board[row_num][col_num] == self.board[row_num + 1][col_num + 1] and self.board[row_num][col_num] == self.board[row_num + 2][col_num + 2] and self.board[row_num][col_num] == self.board[row_num + 3][col_num + 3]:
                    return True
        # loop through the rows on the game board
        for row_num in range(len(self.board) - 1, 2, -1):
            # loop through the columns on the game board
            for col_num in range(len(self.board[row_num]) - 3):
                # checks diagonal bottom left to top right
                if self.board[row_num][col_num] == color and self.board[row_num][col_num] == self.board[row_num - 1][col_num + 1] and self.board[row_num][col_num] == self.board[row_num - 2][col_num + 2] and self.board[row_num][col_num] == self.board[row_num - 3][col_num + 3]:
                    return True
        return False
