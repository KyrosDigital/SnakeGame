'''
    Snake Game Part 4
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
        #0 Append The Snake's range to the Body object for Snakes Body
        for i in range(SNAKE_LENGTH, 0, -1):
            self.body_list.append(Body(x - i, y))

        #1 Define and append the snakes head
        self.body_list.append(Body(x, y, '0'))
        #2 define the window
        self.window = window
        #3 Move snake to right when game starts
        self.direction = KEY_RIGHT
        #4 set snakes lst head coordinate
        self.last_head_coor = (x, y)
        #5 define direction map
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
    #6 Erase all of Body

    #7 Initialize Self aka the body
    def __init__(self, x, y, char='='):
        self.x = x
        self.y = y
        self.char = char
    #8 modify function with special property decorator
    @property
    #9 Set coordinate 
    def coor(self):
        return self.x, self.y

class Food(object):
    def __init__(self):
        self.y = 'Yum, Tasty'

    def method_a(self, foo):
        print self.y + ' ' + foo

food = Food().method_a('Food')
