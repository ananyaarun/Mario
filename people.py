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


class People():
    """ Enemies """

    def __init__(self, xcod, ycod):
        self.xcordi = xcod
        self.ycordi = ycod

    def print_afterenemy(self):
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

    def make_enemy(self):
        self.xcordi += 1
        self.ycordi += 1

        x = rows - 3
        y = randint((columns * 3) - 40, (columns * 6) - 3)


class Enemy1(People):
    """ Enemies """

    def __init__(self, xcod, ycod):
        People.__init__(self, xcod, ycod)
        self.make_enemy()

    def make_enemy(self):
        self.xcordi += 1
        self.ycordi += 1
        for i in range(0, 25):
            x = rows - 3
            y = randint((columns * 3) - 40, (columns * 6) - 3)
            if array[x][y] != '\033[33m' + '#':
                array[x][y] = '\033[37m' + '^'
                array[rows - 4][y] = '\033[37m' + '@'


class Enemy2(People):
    """ Enemies """

    def __init__(self, xcod, ycod, flag):
        People.__init__(self, xcod, ycod)
        self.flag = 0
        self.make_enemy()

    def make_enemy(self):

        x = rows - 3
        y = randint(3, (columns) - 3)
        if array[x][y] != '\033[33m' + '#' and array[x][y] != '^':
            array[x][y] = '\033[36m' + '%'
            array[rows - 4][y] = '\033[36m' + '%'
        self.xcod = x
        self.ycod = y

    def move_enemy2(self, var):
        global start

        array[self.xcod][self.ycod] = ' '
        array[self.xcod][self.ycod - 1] = '\033[36m' + '%'
        array[self.xcod - 1][self.ycod] = ' '
        array[self.xcod - 1][self.ycod - 1] = '\033[36m' + '%'
        self.ycod = self.ycod - 1


class Enemy3(People):
    """ Enemies """

    def __init__(self, xcod, ycod, flag):
        People.__init__(self, xcod, ycod)
        self.flag = 1
        self.make_enemy()

    def make_enemy(self):

        x = rows - 3
        y = randint(3, (columns) - 3)
        if array[x][y] != '\033[33m' + '#' and array[x][y] != '^':
            array[x][y] = '\033[31m' + '$'
            array[rows - 4][y] = '\033[31m' + '$'

        self.xcod = x
        self.ycod = y

    def move_enemy3(self, var):

        array[self.xcod][self.ycod] = ' '
        array[self.xcod][self.ycod + 1] = '\033[31m' + '$'
        array[self.xcod - 1][self.ycod] = ' '
        array[self.xcod - 1][self.ycod + 1] = '\033[31m' + '$'
        self.ycod = self.ycod + 1
