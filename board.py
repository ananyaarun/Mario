import signal
import sys
import tty
import termios
import shutil
import time
from config import *
from colorama import Fore, Back, Style
from random import randint
from colorama import init

init()


class Board():
    """ Background generation """

    def __init__(self):
        self.create_ground()
        self.create_sky()
        self.create_obs()
        self.create_house()
        self.create_mountains()

    def create_ground(self):

        for i in range(0, columns * 6):
            array[rows - 1][i] = '\033[32m' + 'X'
        for i in range(0, columns * 6):
            array[rows - 2][i] = '\033[32m' + 'X'
        for i in range(0, columns * 6):
            array[rows - 13][i] = '\033[32m' + 'X'

    def create_sky(self):
        for i in range(0, 100):
            x = randint(3, 8)
            y = randint(3, (columns * 6) - 3)
            array[x][y] = '\033[34m' + '*'
            array[x][y + 1] = '\033[34m' + '*'
            array[x][y + 2] = '\033[34m' + '*'
            array[x - 1][y + 1] = '\033[34m' + '*'

    def create_obs(self):
        for i in range(0, 20):
            x = rows - 3
            y = randint(3, (columns * 6) - 3)
            array[rows - 5][y] = '\033[33m' + '#'
            array[rows - 6][y] = '\033[33m' + '#'
            array[rows - 7][y] = '\033[33m' + '#'
            array[rows - 5][y + 1] = '\033[33m' + '#'
            array[rows - 6][y + 1] = '\033[33m' + '#'
            array[rows - 8][y + 1] = '\033[35m' + '0'
            array[rows - 7][y + 1] = '\033[33m' + '#'
            array[rows - 5][y + 2] = '\033[33m' + '#'
            array[rows - 6][y + 2] = '\033[33m' + '#'
            array[rows - 7][y + 2] = '\033[33m' + '#'

    def create_house(self):
        x = rows - 12
        y = 6 * columns - 15
        z = 6 * columns - 20
        for i in range(0, 20):
            array[x - i][z] = '|'
        array[x - 20][z] = 'F'
        array[x - 20][z - 1] = 'F'
        array[x - 20][z - 2] = 'F'
        array[x][y] = '-'
        array[x][y + 1] = '-'
        array[x][y + 2] = '-'
        array[x][y + 3] = '-'
        array[x][y + 4] = '-'
        array[x][y + 5] = '-'
        array[x + 1][y] = '|'
        array[x + 2][y] = '|'
        array[x + 3][y] = '|'
        array[x + 1][y + 5] = '|'
        array[x + 2][y + 5] = '|'
        array[x + 3][y + 5] = '|'
        array[x + 4][y] = '-'
        array[x + 4][y + 1] = '-'
        array[x + 4][y + 2] = '-'
        array[x + 4][y + 3] = '-'
        array[x + 4][y + 4] = '-'
        array[x + 4][y + 5] = '-'

    def create_message(sefl):
        global score
        global start
        global lives
        array[2][start + 64] = ' '
        array[2][start + 66] = ' '
        array[2][start + 61] = ' '
        array[2][start + 69] = ' '
        array[2][start + 57] = ' '
        array[2][start + 73] = ' '
        array[2][start + 65] = 'SCORE:' + str(score) + ' LIVES:' + str(lives)

    def create_mountains(self):
        for i in range(0, 60):

            x = rows - 14
            y = randint((columns * 2) - 40, (columns * 6) - 65)
            array[x - 1][y] = '\033[30m' + '&'
            array[x - 1][y + 1] = '\033[30m' + '&'
            array[x - 1][y + 2] = '\033[30m' + '&'
            array[x - 2][y + 1] = '\033[30m' + '&'
            array[x][y] = '\033[30m' + '&'
            array[x][y + 1] = '\033[30m' + '&'
            array[x][y + 2] = '\033[30m' + '&'
            array[x][y - 1] = '\033[30m' + '&'
            array[x][y + 3] = '\033[30m' + '&'

    def print_ground(self):

        for i in range(0, rows):
            string = []
            for j in range(start, stop):
                if array[i][j] != None:
                    string.append(array[i][j])
                else:
                    string.append(' ')
            if string == []:
                print('')

            else:
                print(''.join(string))
