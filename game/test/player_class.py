import math, random, sys
import pygame as py
from pygame.locals import *


# wait for return to be pressed to start game
def pause():
    while True:
        events()
        k = py.key.get_pressed()
        if k[K_RETURN]: break


# exit the game
def events():
    for event in py.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            py.quit()
            sys.exit()


class player:
    def __init__(self, velocity, maxJumpRange):
        self.velocity = velocity
        self.maxJumpRange = maxJumpRange

    def setLocation(self, x, y):
        self.x = x
        self.y = y
        self.xVelocity = 0
        self.jumping = False
        self.jumpcounter = 0
        self.falling = True

    def keys(self):
        k = py.key.get_pressed()

        if k[K_LEFT]:
            self.xVelocity = -self.velocity
        elif k[K_RIGHT]:
            self.xVelocity = self.velocity
        else:
            self.xVelocity = 0

        if k[K_SPACE] and not self.falling:
            self.jumping = True
            self.jumpcounter = 0

    def move(self):
        self.x += self.xVelocity

        # check x boundries

        if self.jumping:
            self.y -= self.velocity
            self.jumpcounter += 1
            if self.jumpcounter == self.maxJumpRange:
                self.jumping = False
                self.falling = True
        elif self.falling:
            if self.y <= height - 10 and self.y + self.velocity >= height - 10:
                self.y = height - 10
                self.falling = False
            else:
                self.y += self.velocity

    def draw(self):
        display = py.display.get_surface()
        py.draw.circle(display, WHITE, (self.x, self.y - 25), 25, 0)

    def do(self):
        self.keys()
        self.move()
        self.draw()


# screen size parameters
(width, height) = (300, 600)
halfWidth, halfHeight = (width // 2), height // 2
AREA = width * height

# initialize the screen
py.init()
CLOCK = py.time.Clock()
DS = py.display.set_mode((width, height))
py.display.set_caption("Player Class")
FPS = 120

# Define Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

def game():

    P = player(3, 10)
    P.setLocation(halfWidth, 0)

    # wait player to hit enter
    pause()

    # Main Loop
    while True:
        events()

        P.do()

        py.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)









if __name__ == '__main__':
    game()
    py.quit()