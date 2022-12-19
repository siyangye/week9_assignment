# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
# by defalut: I make the first user takes O, the second user takes X. 

from numpy import random
#for batabase:
import pandas as pd
import numpy as np
import csv 

# Base class
class Player():
    def move(self, board):
        pass

    def is_bot(self):
        pass

# Extended class for human player
class HumanPlayer(Player):
    def move(self, board):
        # Specifies the row and column index of the cell to move in
        row = int(input()) - 1;
        col = int(input()) - 1;
        # Check if it's a valid move
        while 0 > row or 2 < row or 0 > col or 2 < col or None != board[row][col]:
            print ("Invalid move!")
            row = int(input()) - 1;
            col = int(input()) - 1;

        # Update the game board
        board[row][col] = self

    def is_bot(self):
        return False

# Extended class for bot player
class BotPlayer(Player):
    # Bot is a dummy player, it never try to win, but just follow the basic rule
    def move(self, board):
        while True:
            # Find a random cell to move in
            rnd = random.randint(8)
            row = int(rnd / 3)
            col = int(rnd % 3)
            # Check validity
            if None == board[row][col]:
                break

        board[row][col] = self

    def is_bot(self):
        return True

class Game:
    def __init__(self, O_player, X_player):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        """Remember "dead_player" just used to indicate the situation that the game draws. In such case, "get_winner()" method will return "dead_player" """
        self.dead_player = Player()
        self.O_player = O_player
        self.X_player = X_player
        self.current_player = O_player

    def show_board(self):
        for row in self.board:
            for player in row:
                if self.O_player == player:
                    print('O', end = '')
                elif self.X_player == player:
                    print('X', end = '')
                else:
                    # It's an empty cell
                    print('_', end = '')
            print()

    def check_line(self, first, second, third):
        if None == first:
            if None == second or None == third or second == third:
                return None
            return self.dead_player 

        if first == second and first == third:
            return first

        if first != second and None != second or first != third and None != third:
            return self.dead_player
        return None

    def get_winner(self):
        result = self.dead_player

        # Check 3 "horizonal" lines
        for row in self.board:
            line_result = self.check_line(row[0], row[1], row[2])
            # if a winner found
            if self.O_player == line_result or self.X_player == line_result:
                return line_result
            # if no winner till now but the game will go on
            if None == line_result:
                result = None

        # Check 3 "vertical" lines
        col = 0
        while col < 3:
            line_result = self.check_line(self.board[0][col], self.board[1][col], self.board[2][col])
            if self.O_player == line_result or self.X_player == line_result:
                return line_result
            if None == line_result:
                result = None
            col += 1

        # Check 2 "diagonal" lines
        line_result = self.check_line(self.board[0][0], self.board[1][1], self.board[2][2])
        if self.O_player == line_result or self.X_player == line_result:
            return line_result
        if None == line_result:
            result = None

        line_result = self.check_line(self.board[0][2], self.board[1][1], self.board[2][0])
        if self.O_player == line_result or self.X_player == line_result:
            return line_result
        if None == line_result:
            result = None

        return result

    def run(self):
        winner = None
        while winner == None:
            # If it's a human player, the show the game board and a prompt
            if not self.current_player.is_bot():
                self.show_board()
                print("Take ur turn!")
            self.current_player.move(self.board)
            # Switch turn
            if self.current_player == self.O_player:
                self.current_player = self.X_player
            else:
                self.current_player = self.O_player
            # Get winner
            winner = self.get_winner()

        # Game over. Show the final game board and the winner or 'draw'
        self.show_board()
        if self.O_player == winner:
            print("O wins!")
        elif self.X_player == winner:
            print("X wins!")
        else:
            print("It draws.")


        