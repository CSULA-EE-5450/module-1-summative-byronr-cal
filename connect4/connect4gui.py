from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import numpy as np
from connect4 import *

connect4 = Connect4()


class Connect4Layout(GridLayout):
    """
    Creates the gui layout for the game
    """
    # create cells[row][col]
    # first row
    cell_00 = ObjectProperty(None)
    cell_01 = ObjectProperty(None)
    cell_02 = ObjectProperty(None)
    cell_03 = ObjectProperty(None)
    cell_04 = ObjectProperty(None)
    cell_05 = ObjectProperty(None)
    cell_06 = ObjectProperty(None)
    # second row
    cell_10 = ObjectProperty(None)
    cell_11 = ObjectProperty(None)
    cell_12 = ObjectProperty(None)
    cell_13 = ObjectProperty(None)
    cell_14 = ObjectProperty(None)
    cell_15 = ObjectProperty(None)
    cell_16 = ObjectProperty(None)
    # third row
    cell_20 = ObjectProperty(None)
    cell_21 = ObjectProperty(None)
    cell_22 = ObjectProperty(None)
    cell_23 = ObjectProperty(None)
    cell_24 = ObjectProperty(None)
    cell_25 = ObjectProperty(None)
    cell_26 = ObjectProperty(None)
    # fourth row
    cell_30 = ObjectProperty(None)
    cell_31 = ObjectProperty(None)
    cell_32 = ObjectProperty(None)
    cell_33 = ObjectProperty(None)
    cell_34 = ObjectProperty(None)
    cell_35 = ObjectProperty(None)
    cell_36 = ObjectProperty(None)
    # fifth row
    cell_40 = ObjectProperty(None)
    cell_41 = ObjectProperty(None)
    cell_42 = ObjectProperty(None)
    cell_43 = ObjectProperty(None)
    cell_44 = ObjectProperty(None)
    cell_45 = ObjectProperty(None)
    cell_46 = ObjectProperty(None)
    # sixth row
    cell_50 = ObjectProperty(None)
    cell_51 = ObjectProperty(None)
    cell_52 = ObjectProperty(None)
    cell_53 = ObjectProperty(None)
    cell_54 = ObjectProperty(None)
    cell_55 = ObjectProperty(None)
    cell_56 = ObjectProperty(None)

    def __init__(self, *args, **kwargs):

        super(Connect4Layout, self).__init__(*args, **kwargs)

        self.cells = {
            0: self.cell_00,
            1: self.cell_01,
            2: self.cell_02,
            3: self.cell_03,
            4: self.cell_04,
            5: self.cell_05,
            6: self.cell_06,
            10: self.cell_10,
            11: self.cell_11,
            12: self.cell_12,
            13: self.cell_13,
            14: self.cell_14,
            15: self.cell_15,
            16: self.cell_16,
            20: self.cell_20,
            21: self.cell_21,
            22: self.cell_22,
            23: self.cell_23,
            24: self.cell_24,
            25: self.cell_25,
            26: self.cell_26,
            30: self.cell_30,
            31: self.cell_31,
            32: self.cell_32,
            33: self.cell_33,
            34: self.cell_34,
            35: self.cell_35,
            36: self.cell_36,
            40: self.cell_40,
            41: self.cell_41,
            42: self.cell_42,
            43: self.cell_43,
            44: self.cell_44,
            45: self.cell_45,
            46: self.cell_46,
            50: self.cell_50,
            51: self.cell_51,
            52: self.cell_52,
            53: self.cell_53,
            54: self.cell_54,
            55: self.cell_55,
            56: self.cell_56
        }
        self.current_player = connect4.player_1
        self.board = connect4.create_board()
        connect4.flip_board(self.board)
        self.game_over = False
        self.turn = 0

    def select(self, row_num, col_num, cell_num):

        if connect4.move_is_valid(self.board, row_num, col_num):
            connect4.place_piece(self.board, row_num, col_num, self.current_player)
            self.set_piece(cell_num, self.current_player)

    def set_piece(self, cell, player):
        self.cells[cell].background_normal = 'images/%s.png' % player
        if connect4.check_win(self.board, player):
            # display win?
            self.game_over = True

        if self.current_player == connect4.player_1:
            self.current_player == connect4.player_2
        else:
            self.current_player == connect4.player_1
