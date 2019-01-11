import signal
import sys
import tty
import termios
import shutil
import time
import os
from config import *
from mario import *
from people import *
from board import *
from colorama import Fore, Back, Style
from random import randint
from colorama import init

init()

class GetchUnix():
    """ input """

    def __init__(self):
        pass

    def __call__(self):
        fd_move = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd_move)
        try:
            tty.setraw(sys.stdin.fileno())
            ch_move = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd_move, termios.TCSADRAIN, old_settings)
        return ch_move


class AlarmException(Exception):
    """ exception """
    pass


getch = GetchUnix()


def alarm_handler(_signum, _frame):
    """	alarm """
    raise AlarmException


def input_to(timeout=1):
    """ input """
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def print_game():

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


def print_mess():
    global score
    global start
    global lives
    global level
    array[2][start + 64] = ' '
    array[2][start + 66] = ' '
    array[2][start + 61] = ' '
    array[2][start + 69] = ' '
    array[2][start + 57] = ' '
    array[2][start + 73] = ' '
    array[2][start + 65] = 'SCORE:' + \
        str(score) + ' LIVES:' + str(lives) + ' LEVEL:' + str(level)


def main():
    """ main class """
    global score
    current_board = Board()
    current_char = Mario()
    current_enemy = Enemy1(0, 0)
    current_enemies = []
    for i in range(0, 3):
        current_enemies.append(Enemy2(0, 0, 0))
    current_enemies3 = []
    for i in range(0, 3):
        current_enemies3.append(Enemy3(0, 0, 1))

    global start
    global stop
    global lives
    global check
    global level
    print_game()
    print_mess()
    os.system("aplay 4.wav&")

    while True:

        if start + 65 > columns * 2 - 40:
            level = 2

        if start + 65 > columns * 4 - 40:
            level = 3

        if start + 65 > (columns * 6) - 75:
            current_char.mario_end()
            print('CONGRATS YOU WON !!!! UR SCORE IS: ' + str(score))
            sys.exit(0)

        if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%' and array[rows - 5][start + 65] != '\033[33m' + '#' and array[rows - 4][start + 65] != ' ' and check != 1:
            lives = lives - 1
            if lives == 0:
                lives = 0
                print_mess()
                os.system("aplay 3.wav&")
                print("THE END U LOST :(")
                sys.exit()
        inp = input_to()
        if inp == 'q':
            sys.exit(0)
        if inp == 'd':

            if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%' or array[rows - 4][start + 65] == '\033[33m' + '#':
                lives = lives - 1
                if lives == 0:
                    lives = 0
                    print_mess()
                    os.system("aplay 3.wav&")
                    print("THE END U LOST :(")
                    sys.exit()

            if array[rows - 7][start + 65] == '\033[33m' + '#':
                array[rows - 8][start + 65] = ' '
                array[rows - 9][start + 65] = ' '
                array[rows - 10][start + 65] = ' '

            else:
                array[rows - 4][start + 65] = ' '
                array[rows - 5][start + 65] = ' '
                array[rows - 6][start + 65] = ' '
            start = start + 1
            stop = stop + 1
            print_game()

            if array[rows - 4][start + 65] == '\033[37m' + '@' or array[rows - 8][start + 65] == '\033[35m' + '0':
                os.system("aplay 2.wav&")
                score += 1

            if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%':
                lives = lives - 1
                if lives == 0:
                    lives = 0
                    print_mess()
                    os.system("aplay 3.wav&")
                    print("THE END U LOST :(")
                    sys.exit()

            if array[rows - 7][start + 65] == '\033[33m' + '#':
                array[rows - 8][start + 65] = 'M'
                array[rows - 9][start + 65] = 'O'
                array[rows - 10][start + 65] = '/'
            else:
                array[rows - 4][start + 65] = 'M'
                array[rows - 5][start + 65] = 'O'
                array[rows - 6][start + 65] = '/'

            print_game()
            print_mess()

        if inp == 'a':

            if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%' or array[rows - 4][start + 65] == '\033[33m' + '#':
                lives = lives - 1
                if lives == 0:
                    lives = 0
                    print_mess()
                    os.system("aplay 3.wav&")
                    print("THE END U LOST :(")
                    sys.exit()

            if array[rows - 7][start + 65] == '\033[33m' + '#':
                array[rows - 8][start + 65] = ' '
                array[rows - 9][start + 65] = ' '
                array[rows - 10][start + 65] = ' '
            else:
                array[rows - 4][start + 65] = ' '
                array[rows - 5][start + 65] = ' '
                array[rows - 6][start + 65] = ' '

            start = start - 1
            stop = stop - 1

            if array[rows - 4][start + 65] == '\033[37m' + '@' or array[rows - 8][start + 65] == '\033[35m' + '0':
                os.system("aplay 2.wav&")
                score += 1
            if array[rows - 4][start + 65] == '\033[31m' + '$' or array[rows - 4][start + 65] == '\033[36m' + '%':
                lives = lives - 1
                if lives == 0:
                    os.system("aplay 3.wav&")
                    print("THE END U LOST :(")

                    sys.exit()

            if array[rows - 7][start + 65] == '\033[33m' + '#':
                array[rows - 8][start + 65] = 'M'
                array[rows - 9][start + 65] = 'O'
                array[rows - 10][start + 65] = '/'

            else:
                array[rows - 4][start + 65] = 'M'
                array[rows - 5][start + 65] = 'O'
                array[rows - 6][start + 65] = '/'

            print_game()
            print_mess()

        if inp == 'w':
            if array[rows - 7][start + 65] != '\033[33m' + '#':

                array[rows - 4][start + 65] = ' '
                array[rows - 5][start + 65] = ' '
                array[rows - 6][start + 65] = ' '

                start = start + 4
                stop = stop + 4

                if array[rows - 7][start + 65] == '\033[33m' + '#':
                    array[rows - 8][start + 65] = 'M'
                    array[rows - 9][start + 65] = 'O'
                    array[rows - 10][start + 65] = '/'
                else:
                    array[rows - 8][start + 65] = 'M'
                    array[rows - 9][start + 65] = 'O'
                    array[rows - 10][start + 65] = '/'
                    print_game()
                    time.sleep(0.5)
                    array[rows - 8][start + 65] = ' '
                    array[rows - 9][start + 65] = ' '
                    array[rows - 10][start + 65] = ' '
                    start = start + 4
                    stop = stop + 4
                    print_game()
                    array[rows - 6][start + 65] = 'M'
                    array[rows - 7][start + 65] = 'O'
                    array[rows - 8][start + 65] = '/'

                    print_game()
                    time.sleep(0.3)
                    array[rows - 6][start + 65] = ' '
                    array[rows - 7][start + 65] = ' '
                    array[rows - 8][start + 65] = ' '

                    if array[rows - 4][start + 65] == '\033[31m' + '$':
                        score = score + 10

                    if array[rows - 4][start + 65] == '\033[36m' + '%':
                        score = score + 10
                        check = 1

                    array[rows - 4][start + 65] = 'M'
                    array[rows - 5][start + 65] = 'O'
                    array[rows - 6][start + 65] = '/'
                    print_game()

                print_game()
                print_mess()

        for i in range(0, len(current_enemies)):
            if check != 1:
                current_enemies[i].move_enemy2(0)
                print_game()
                print_mess()

        for i in range(0, len(current_enemies3)):

            current_enemies3[i].move_enemy3(0)
            print_game()
            print_mess()


if __name__ == "__main__":
    main()
