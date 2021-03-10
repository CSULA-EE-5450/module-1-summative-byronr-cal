import kivy

kivy.require('2.0.0')
from connect4gui import *
from kivy.app import App


class Connect4App(App):

    def build(self):
        return Connect4Layout(cols=7, rows=6)


if __name__ == '__main__':
    Connect4App().run()
