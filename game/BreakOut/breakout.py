# Break out Game by Benji Charles #

import math, random, sys
import pygame as py
from pygame.locals import *


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


class player:
    def __init__(self, velocity):
        self.velocity = velocity
        self._width = halfWidth // 3
        self._height = 10
        self.x = halfWidth - (self._width//2)
        self.y = height - 50

    def movement(self):
        # get the keys the the user presses
        move = py.key.get_pressed()

        # user moving left
        if move[K_LEFT]:
            self.x -= self.velocity
        # user moving right
        elif move[K_RIGHT]:
            self.x += self.velocity

        # if the user goes to far right
        if self.x > width - self._width:
            self.x = width - self._width

        # if the user goes to far left
        if self.x < 0:
            self.x = 0

    def draw(self):
        display = py.display.get_surface()
        py.draw.rect(display, WHITE, (self.x, self.y, self._width, self._height), 0)

    def do(self):
        self.movement()
        self.draw()

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width


class ball:
    def __init__(self, velocity):
        self.velocity = velocity
        self.x = halfWidth
        self.y = height - 50
        self.dx = -2
        self.dy = -3
        self._radius = 5
        self.boarder = 20

    def movement(self):
        self.x += self.dx * self.velocity
        self.y += self.dy * self.velocity

        if self.y < self.boarder:
            self.dy *= -1

        if self.x < self.boarder or self.x > width - self.boarder:
            self.dx *= -1

        if self.y > height:
            print("GAME OVER")
            py.quit()
            sys.exit()

    def draw(self):
        display = py.display.get_surface()
        py.draw.circle(display, RED, (self.x, self.y), self._radius, 0)

    def do(self):
        self.movement()
        self.draw()


# screen size parameters
(width, height) = (600, 500)
halfWidth, halfHeight = width // 2, height // 2
AREA = width * height

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 0)


def breakout():

    # initialize pygame
    py.init()
    CLOCK = py.time.Clock()
    DS = py.display.set_mode((width, height))
    py.display.set_caption("BreakOut")
    FPS = 20

    # wait player to hit enter
    pause()

    P = player(15)
    B = ball(6)

    run = True

    # Main Loop
    while run:
        events()

        P.do()
        B.do()

        for i in range(B.y, B.y + (B.dy * B.velocity)):
            if i > P.y and (P.x <= B.x <= P.x + P.width):
                B.dy *= -1

        py.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)


if __name__ == '__main__':
    breakout()
    py.quit()
