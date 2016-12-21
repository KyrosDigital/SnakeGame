'''
    Snake Game Part 1
'''

''' #1 import some stuff '''
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_DOWN, KEY_UP
from random import randint

''' #2 Define some variables '''
WIDTH = 35
HEIGHT = 20
MAX_X = WIDTH - 2
MAX_Y = HEIGHT - 2
SNAKE_LENGTH = 5
SNAKE_X = SNAKE_LENGTH + 1
SNAKE_Y = 3
TIMEOUT = 100

''' #3 make Snake Oject '''
class Snake(object):
    def __init__(self):
        self.x = 'Hisss!'

    def method_a(self, foo):
        print self.x + ' ' + foo

snake = Snake()               # We do not pass any argument to the __init__ method
snake.method_a('Says the snake') # We only pass a single argument
