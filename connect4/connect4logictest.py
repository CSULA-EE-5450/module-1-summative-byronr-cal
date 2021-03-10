import numpy as np

num_columns = 7
num_rows = 6
top_row_idx = 5
player_1 = 1
player_2 = 2


def create_board():
    """
    Creates the board so that pieces can be placed

    :return: board that is an array of zeros where pieces can be placed
    """
    board = np.zeros((6, 7))
    return board


def flip_board(board):
    """
    Flips the board so that the array logically matches a connect4 board

    :param board: board used to play the game
    :return:
    """
    print(np.flip(board, 0))


def place_piece(board, row, column, player):
    """
    Places a piece on the board that represents the player

    :param board: board used to play the game
    :param row: idx for the row
    :param column: idx for the column
    :param player: player that is placing the piece
    :return:
    """
    board[row][column] = player


def move_is_valid(board, column):
    """
    Checks if location selected is empty and can be used

    :param board: board used to play the game
    :param column:
    :return:
    """
    return board[top_row_idx][column] == 0


def next_row(board, column):
    """
    Gets next available row

    :param board: board used to play the game
    :param column: Column selected by the player
    :return: Next available row piece can be dropped in
    """
    for row in range(num_rows):
        if board[row][column] == 0:
            return row


def check_win(board, piece):
    """
    Checks for win

    :param board: board used to play the game
    :param piece: Player's piece
    :return: winning move
    """
    # horizontal wins
    for column in range(num_columns - 3):
        for row in range(num_rows):
            if board[row][column] == piece and board[row][column + 1] and board[row][column + 2] and board[row][column + 3]:
                return True
    # vertical wins
    for column in range(num_columns):
        for row in range(num_rows - 3):
            if board[row][column] == piece and board[row + 1][column] and board[row + 2][column] and board[row + 3][column]:
                return True

    # diagonal forward
    for column in range(num_columns - 3):
        for row in range(num_rows - 3):
            if board[row][column] == piece and board[row + 1][column + 1] and board[row + 2][column + 2] and \
                    board[row + 3][column + 3]:
                return True

    # diagonal backwards
    for column in range(num_columns - 3):
        for row in range(3, num_rows):
            if board[row][column] == piece and board[row - 1][column + 1] and board[row - 2][column + 2] and \
                    board[row - 3][column + 3]:
                return True


board = create_board()
flip_board(board)
game_over = False
turn = 0

while not game_over:
    # player one moves
    if turn == 0:
        col_selected = int(input("Player 1 make your move 0-6"))

        if move_is_valid(board, col_selected):
            open_row = next_row(board, col_selected)
            place_piece(board, open_row, col_selected, player_1)

            if check_win(board, player_1):
                print("Player 1 wins")
                game_over = True

    else:
        # player 2 moves
        col_selected = int(input("Player 2 make your move 0-6"))

        if move_is_valid(board, col_selected):
            open_row = next_row(board, col_selected)
            place_piece(board, open_row, col_selected, player_2)

            if check_win(board, player_2):
                print("Player 2 wins")
                game_over = True

    flip_board(board)

    turn += 1
    turn = turn % 2
