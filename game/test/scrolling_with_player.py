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


def game():


    # wait player to hit enter
    pause()

    stageWidth = bkgdWidth * 10
    stagePosX = 0
    startScrollPosX = halfWidth

    circleRadius = 20
    circlePosX = circleRadius

    playerPosX = circleRadius
    playerPosY = 500
    playerVelocityX = 0

    # Main Loop
    while True:
        events()

        k = py.key.get_pressed()
        if k[K_RIGHT]:
            playerVelocityX = 20
        elif k[K_LEFT]:
            playerVelocityX = -20
        else:
            playerVelocityX = 0

        playerPosX += playerVelocityX

        # playing going to far right
        if playerPosX > stageWidth - circleRadius:
            playerPosX = stageWidth - circleRadius

        # player going to far left
        if playerPosX < circleRadius:
            playerPosX = circleRadius

        # positioning the circle on the display surface and moving the stage
        if playerPosX < startScrollPosX:
            circlePosX = playerPosX
        elif playerPosX > stageWidth - startScrollPosX:
            circlePosX = playerPosX - stageWidth + width
        else:
            circlePosX = startScrollPosX
            stagePosX += -playerVelocityX


        rel_x = stagePosX % bkgdWidth

        # display background
        DS.blit(bkgd, (rel_x - bkgdWidth, 0))
        if rel_x < width:
            DS.blit(bkgd, (rel_x, 0))

        py.draw.circle(DS, WHITE, (circlePosX, playerPosY - circleRadius), circleRadius, 0)


        py.display.update()
        CLOCK.tick(FPS)
        DS.fill(BLACK)


# screen size parameters
(width, height) = (600, 576)
halfWidth, halfHeight = (width // 2), height // 2
AREA = width * height

# initialize the screen
py.init()
CLOCK = py.time.Clock()
DS = py.display.set_mode((width, height))
py.display.set_caption("Scrolling with Player")
FPS = 500

# Define Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

bkgd = py.image.load("rsz_bg1.png").convert()
bkgdWidth, bkgdHeight = bkgd.get_rect().size







if __name__ == '__main__':
    game()
    py.quit()