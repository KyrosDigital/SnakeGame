'''
    Snake Game Part 7
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

    ''' In this section we need to finish the snake object.
    If we run this program in the console, currently it will output an error '''

    #0 add_body function, this adds the snake body
    def add_body(self, body_list):
        # append() : It is basically used in python to add, one element.
        # extend() : Where extend(), is used to merged to lists or insert multiple elements in one list.
        self.body_list.extend(body_list)

    #1 Eat food fucntion, functionalty for snake eating food
    def eat_food(self, food):
        # reset food
        food.reset()
        # choosing x y coordinates for the new body part on the snke
        body = Body(self.last_head_coor[0], self.last_head_coor[1])
        # adding above variable to the body array on the snake
        self.body_list.insert(-1, body)
        # update game score
        self.hit_score += 1
        # this is a timer function. note, we shold play with this to see what it acutally does
        if self.hit_score % 3 == 0:
            self.timeout -= 5
            self.window.timeout(self.timeout)

    #2 Add new property decorator
    @property
    def collided(self): # Body collided function, if snake head hits body part end game
        return any([body.coor == self.head.coor
                    for body in self.body_list[:-1]])

    #3 Make Updating function for animation
    def update(self):
        # pop() removes and returns last object or obj from the list.
        last_body = self.body_list.pop(0)
        # setting x and y for the snake head
        last_body.x = self.body_list[-1].x
        last_body.y = self.body_list[-1].y
        self.body_list.insert(-1, last_body)
        # set last head coordinate
        self.last_head_coor = (self.head.x, self.head.y)
        # grab direction map from above, set its direction on update
        self.direction_map[self.direction]()

    #4 change direction function
    def change_direction(self, direction):
        # grab REV DIR MAP from above
        if direction != Snake.REV_DIR_MAP[self.direction]:
            self.direction = direction
    #5 Make Render Function
    def render(self):
        for body in self.body_list:
            # add snake body to window. We call this render function while true
            self.window.addstr(body.y, body.x, body.char)

    #6 Make new property decorator
    @property
    # define the snake head
    def head(self):
        # snake head should always be the first in the body list, thats why its negative here
        return self.body_list[-1]

    #7 set snake head initial coordinate
    @property
    def coor(self):
        return self.head.x, self.head.y

    #8 Make move up function
    def move_up(self):
        self.head.y -= 1
        if self.head.y < 1:
            self.head.y = MAX_Y
    #9 move down
    def move_down(self):
        self.head.y += 1
        if self.head.y > MAX_Y:
            self.head.y = 1
    #10 move left
    def move_left(self):
        self.head.x -= 1
        if self.head.x < 1:
            self.head.x = MAX_X
    #11 move rigth
    def move_right(self):
        self.head.x += 1
        if self.head.x > MAX_X:
            self.head.x = 1

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


if __name__ == '__main__':
    curses.initscr()
    curses.beep()
    curses.beep()
    window = curses.newwin(HEIGHT, WIDTH, 0, 0)
    window.timeout(TIMEOUT)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)

    snake = Snake(SNAKE_X, SNAKE_Y, window)
    food = Food(window, '*')

    while True:
        window.clear()
        window.border(0)
        snake.render()
        food.render()
        #12 addstr to the window
        window.addstr(0, 5, snake.score)
        #13 getch() (gets a character from user input
        event = window.getch()


    curses.endwin()
