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


class Mario():

    def __init__(self):

        self.__first = 'M'
        self.__sec = 'O'
        self.__third = '/'

    def create_mariof(self):
        global start
        global score
        if array[rows - 4][start + 65] == '\033[37m' + '@' or array[rows - 8][start + 65] == '\033[35m' + '0':
            score += 1

        if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%':
            sys.exit()

        if array[rows - 7][start + 65] == '\033[33m' + '#':
            array[rows - 8][start + 65] = 'M'
            array[rows - 9][start + 65] = 'O'
            array[rows - 10][start + 65] = '/'
        else:
            array[rows - 4][start + 65] = 'M'
            array[rows - 5][start + 65] = 'O'
            array[rows - 6][start + 65] = '/'

    def create_mariob(self):
        global start
        global score

        if array[rows - 4][start + 65] == '\033[37m' + '@' or array[rows - 8][start + 65] == '\033[35m' + '0':
            score += 1
        if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%':
            sys.exit()

        if array[rows - 7][start + 65] == '\033[33m' + '#':
            array[rows - 8][start + 65] = 'M'
            array[rows - 9][start + 65] = 'O'
            array[rows - 10][start + 65] = '/'

        else:
            array[rows - 4][start + 65] = 'M'
            array[rows - 5][start + 65] = 'O'
            array[rows - 6][start + 65] = '/'

    def others(self):
        time.sleep(0.5)
        self.jumpsleep()
        self.print_afterjump()
        self.jumpdown()
        self.print_afterjump()

    def jumpup(self):
        global start
        if array[rows - 7][start + 65] == '\033[33m' + '#':
            array[rows - 8][start + 65] = 'M'
            array[rows - 9][start + 65] = 'O'
            array[rows - 10][start + 65] = '/'
        else:
            array[rows - 8][start + 65] = 'M'
            array[rows - 9][start + 65] = 'O'
            array[rows - 10][start + 65] = '/'

    def jumpdown(self):
        global start
        global score
        array[rows - 6][start + 65] = 'M'
        array[rows - 7][start + 65] = 'O'
        array[rows - 8][start + 65] = '/'

        self.print_afterjump()
        time.sleep(0.3)
        array[rows - 6][start + 65] = ' '
        array[rows - 7][start + 65] = ' '
        array[rows - 8][start + 65] = ' '

        if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%':
            score = score + 10
            check = 1

        array[rows - 4][start + 65] = 'M'
        array[rows - 5][start + 65] = 'O'
        array[rows - 6][start + 65] = '/'

    def jumpsleep(self):
        global start
        global stop

        array[rows - 8][start + 65] = ' '
        array[rows - 9][start + 65] = ' '
        array[rows - 10][start + 65] = ' '
        start = start + 4
        stop = stop + 4

    def mario_end(self):

        array[rows - 4][start + 65] = ' '
        array[rows - 5][start + 65] = ' '
        array[rows - 6][start + 65] = ' '

        x = rows - 19
        y = 6 * columns - 21

        array[x][y] = 'M'
        array[x - 1][y] = 'O'
        array[x - 2][y] = '/'

    def print_afterjump(self):

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
