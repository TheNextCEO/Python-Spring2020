# importing the libraries and setting the global variables

import math, random, sys
import pygame as py
from pygame.locals import *


# define the colors

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 225)
green = (0, 225, 0)
red = (225, 0, 0)

# define the size of the blocks

block_width = 23
block_height = 15


# wait for return to be pressed to start game
def pause():
    while True:
        events()
        k = py.key.get_pressed()
        if k[K_RETURN]:
            break


# exit the game
def events():
    for event in py.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            py.quit()
            sys.exit()


class Block(py.sprite.Sprite):
    """ this class respresent each block that gets knocked out"""
    def __init__(self, color, x, y):
        # call the parent sprite class constructor
        super().__init__()

        # make an image of block of appropriate size
        self.image = py.SurfaceType([block_width, block_height])

        # fill the image with the color
        self.image.fill(color)

        # fetch the retangle object demensions of the image
        self.rect = self.image.get_rect()

        # move the top left of the rectangle to x,y
        # where the block will appear
        self.rect.x = x
        self.rect.y = y


class Ball(py.sprite.Sprite):
    """ This class is for the ball """
    # speed of the pixels per cycle
    speed = 10.0

    # floating point representation of where the ball is
    x = 0.0
    y = 180.0

    # direction of ball ( in degrees )
    direction = 200
    width = 10
    height = 10

    # contructor
    def __init__(self):
        # call the parent class (sprite) constructor
        super().__init__()

        # create the image of the ball
        self.image = py.Surface([self.width, self.height])

        # color of the ball
        self.image.fill(white)

        # get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()

        # getting the screen attributes for height/width
        self.screenheight = py.display.get_surface().get_height()
        self.screenwidth = py.display.get_surface().get_width()

    def bounce(self, diff):
        """This function will bounce the ball in the opposite direction"""

        self.direction = (180 - self.direction) % 360
        self.direction -= diff

    def update(self):
        """Updating the position of the ball"""

        # convert into degrees
        direction_radians = math.radians(self.direction)

        # change the position of x and y according to speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)

        # move the image
        self.rect.x = self.x
        self.rect.y = self.y
        print(self.x, self.y)

        # test if the ball bounced off the top
        if self.y <= 0:
            self.bounce(0)
            self.y = 1

        # test if the ball bounced off the left of the screen
        if self.x <= 0:
            self.direction = (360 - self.direction) % 360
            self.x = 1

        # test if the ball bounced off the right of the screen
        if self.x > self.screenwidth - self.width:
            self.direction = (360 - self.direction) % 360
            self.x = self.screenwidth - self.width - 1

        # test if the ball hit the bottom
        if self.y > 600:
            return True
        else:
            return False





def breakout():
    # initialize pygame
    py.init()

    # create an 800X600 screen
    screen = py.display.set_mode([800,600])

    # set then title of the window
    py.display.set_caption("Breakout")

    # make the mouse disappear
    py.mouse.set_visible(0)

    # font for text
    font = py.font.Font(None, 36)

    # making the surface to draw on
    background = py.Surface(screen.get_size())

    # creating sprite lists
    blocks = py.sprite.Group()
    balls = py.sprite.Group()
    allsprites = py.sprite.Group()

    # create the ball
    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    # the top of the blocks (y position)
    top = 80

    # the numbers of blocks to make
    blockcount = 32

    # --- Create blocks

    # five rows of blocks
    for row in range(5):
        # 32 clomns of blocks
        for column in range(0, blockcount):
            # create a block (color, x, y)
            block = Block(blue, column * (block_width + 2) + 1, top)
            blocks.add(block)
            allsprites.add(block)
        # move the top of the next row down
        top += block_width + 2

    # clock to limit speed
    clock = py.time.Clock()

    # is the game over?
    game_over = False

    # exit the game?
    exit_program = False

    # wait player to hit enter
    # pause()

    while not exit_program:
        events()

        # limit to 30 fps
        clock.tick(30)

        # clear the screen
        screen.fill(black)

        # update the ball
        if not game_over:
            game_over = ball.update()

        # draw everything
        allsprites.draw(screen)

        # flip the screen and show is drawn
        py.display.flip()


if __name__ == '__main__':
    breakout()
    py.quit()
