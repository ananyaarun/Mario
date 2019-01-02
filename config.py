import signal
import sys
import tty
import termios
import shutil
import time
from colorama import Fore, Back, Style
from random import randint
from colorama import init

init()
rows = shutil.get_terminal_size().lines
columns = shutil.get_terminal_size().columns
string = []
array = [[None for _ in range(columns * 6)] for _ in range(rows)]
start = 0
stop = columns
score = 0
lives = 3
check = 0
level = 1
