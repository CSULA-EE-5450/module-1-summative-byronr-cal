import numpy as np


class Connect4(object):
    """ Connect4 game object
    """
    def __init__(self):
        """
        Connect 4 object constructor
        """
        self.num_columns = 7
        self.num_rows = 6
        self.top_row_idx = 5
        self.player_1 = 1
        self.player_2 = 2

    def create_board(self):
        """
        Creates the board so that pieces can be placed

        :return: board that is an array of zeros where pieces can be placed
        """
        board = np.zeros((6, 7))
        return board

    def flip_board(self, board):
        """
        Flips the board so that the array logically matches a connect4 board

        :param board: board used to play the game
        :return:
        """
        print(np.flip(board, 0))

    def place_piece(self, board, row, column, player):
        """
        Places a piece on the board that represents the player

        :param board: board used to play the game
        :param row: idx for the row
        :param column: idx for the column
        :param player: player that is placing the piece
        :return:
        """
        board[row][column] = player

    def move_is_valid(self, board, row, column):
        """
        Checks if location selected is empty and can be used

        :param board: board used to play the game
        :param row: row of button selected by player
        :param column: column of button selected by player
        :return: True if valid move
        """
        return board[row][column] == 0

    def next_row(self, board, column):
        """
        Gets next available row

        :param board: board used to play the game
        :param column: Column selected by the player
        :return: Next available row piece can be dropped in
        """
        for row in range(self.num_rows):
            if board[row][column] == 0:
                return row

    def check_win(self, board, piece):
        """
        Checks for win

        :param board: board used to play the game
        :param piece: Player's piece
        :return: winning move
        """
        # horizontal wins
        for column in range(self.num_columns - 3):
            for row in range(self.num_rows):
                if board[row][column] == piece and board[row][column + 1] and board[row][column + 2] and board[row][column + 3]:
                    return True
        # verticle wins
        for column in range(self.num_columns):
            for row in range(self.num_rows - 3):
                if board[row][column] == piece and board[row + 1][column] and board[row + 2][column] and board[row + 3][column]:
                    return True

        # diagonal forward
        for column in range(self.num_columns - 3):
            for row in range(self.num_rows - 3):
                if board[row][column] == piece and board[row + 1][column + 1] and board[row + 2][column + 2] and \
                        board[row + 3][column + 3]:
                    return True

        # diagonal backwards
        for column in range(self.num_columns - 3):
            for row in range(3, 6):
                if board[row][column] == piece and board[row - 1][column + 1] and board[row - 2][column + 2] and \
                        board[row - 3][column + 3]:
                    return True

