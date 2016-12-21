'''
    Snake Game Part 3
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
    #0 Erase everything in snake object
    #1  Add REV_DIR_MAP
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }
    #2 def Init, set score to 0, set timeout, body list
    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = TIMEOUT

    #3 Make Properties on the objects,
    #which is a special decorator that modifies
    #the function. makes it so when you access the attribute,
    #it auto calls the function. Makes for more reusable code
    @property
    def score(self):
        # the new way of formating with python,  https://pyformat.info/
        # example: '{} {}'.format('one', 'two') ==> "one two"
        return 'Score : {}'.format(self.hit_score)


class Body(object):
    def __init__(self):
        self.x = 'this is the'

    def method_a(self, foo):
        print self.x + ' ' + foo

body = Body().method_a('Body')


class Food(object):
    def __init__(self):
        self.y = 'Yum, Tasty'

    def method_a(self, foo):
        print self.y + ' ' + foo

food = Food().method_a('Food')
