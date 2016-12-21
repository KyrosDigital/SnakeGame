'''
    Snake Game Part 2
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
    def __init__(self):
        self.x = 'Hisss!'

    def method_a(self, foo):
        print self.x + ' ' + foo

snake = Snake()               # We do not pass any argument to the __init__ method
snake.method_a('Says the snake') # We only pass a single argument

''' #1 make Body Oject '''
class Body(object):
    def __init__(self):
        self.x = 'this is the'

    def method_a(self, foo):
        print self.x + ' ' + foo

body = Body().method_a('Body')

''' #2 make Food Oject '''
class Food(object):
    def __init__(self):
        self.y = 'Yum, Tasty'

    def method_a(self, foo):
        print self.y + ' ' + foo

food = Food().method_a('Food')
