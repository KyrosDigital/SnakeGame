'''
    Snake Game Part 6
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
    def __init__(self, window, char='&'):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)
        self.char = char
        self.window = window

    def render(self):
        self.window.addstr(self.y, self.x, self.char)

    def reset(self):
        self.x = randint(1, MAX_X)
        self.y = randint(1, MAX_Y)

'''
When the Python interpreter reads a source file, it executes all of the code found in it.
Before executing the code, it will define a few special variables. For example,
if the python interpreter is running that module (the source file) as the main program,
it sets the special __name__ variable to have a value "__main__".
If this file is being imported from another module, __name__ will be set to the module's name.
'''
#0 since this is the source file for our program, we set the __name__  Variable to __main__
if __name__ == '__main__':
    ''' Before doing anything, curses must be initialized.
    This is done by calling the initscr() function,
    which will determine the terminal type, send any required
    setup codes to the terminal, and create various internal data structures.
    If successful, initscr() returns a window object representing the entire screen;
    this is usually called stdscr, after the name of the corresponding C variable. '''
    #1 Special Curses Function for initializing Curses
    curses.initscr()
    #1.1 Make Beeping Noise twice
    curses.beep()
    curses.beep()

    ''' Windows are the basic abstraction in curses. A window object represents
    a rectangular area of the screen, and supports various methods to display
    text, erase it, allow the user to input strings, and so forth. '''
    #2 Make Curses Window
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    #3 Set windo timeout
    window.timeout(TIMEOUT)
    #4 Set keypad
    window.keypad(1)
    #5 Leave echo mode. Echoing of input characters is turned off. https://docs.python.org/3/library/curses.html
    curses.noecho()
    #6 set curses visibility state https://docs.python.org/3/library/curses.html
    curses.curs_set(0)
    #7 set window border
    window.border(0)

    #7.5 grab snake and food object
    snake = Snake(SNAKE_X, SNAKE_Y, window)
    food = Food(window, '*')

    #8 Create while true Function
    while True:
        #8.1 clear window
        window.clear()
        #8.2 set border
        window.border(0)
        #8.3 render snake
        snake.render()
        #8.4 render food
        food.render()
        #12 addstr to the window
        window.addstr(0, 5, snake.score)
        #13 getch() (gets a character from user input
        event = window.getch()
    #9 end curses while no longer true
    curses.endwin()
