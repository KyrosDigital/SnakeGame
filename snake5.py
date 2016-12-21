'''
    Snake Game Part 5
'''

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

class Snake(object):
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT

        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))

        self.body_list.append(Body(x, y, '0'))
        self.window = window
        self.direction = KEY_RIGHT
        self.last_head_coor = (x, y)
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
        }

    @property
    def score(self):
        return 'Score : {}'.format(self.hit_score)

class Body(object):
    def __init__(self, x, y, char='='):
        self.x = x
        self.y = y
        self.char = char

    @property
    def coor(self):
        return self.x, self.y

class Food(object):
    #0 Erase all of food object

    #1 Initalize the Food
    def __init__(self, window, char='&'):
        #2 choose random postion for food whenever its Initalized Boiiii
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        #3 here, we are just satifying the arguments, and setting the food character
        self.char = char
        self.window = window

    #4 Make Render Function
    def render(self):
        #5 This is using addstr, which is part of Curses Programing in Python, see https://docs.python.org/2/howto/curses.html
        ''' Because this is all going to be animated in the terminal via Curses, we use addstr to display the & character
        The addstr() function takes a Python string as the value to be displayed,
        while the addch() functions take a character, which can be either a Python string of length 1 or an integer
        If it is a string, your limited to displaying characters between 0 and 255 0 and 255
        in summary, this is adding food coordinates and character in string format when rendered '''
        self.window.addstr(self.y, self.x, self.char)
    #6 reset method, chooses new random coordinates when reset
    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
