# Snake by Daimeun Praytor

import sys, random
import pygame as py
from pygame.locals import *


# Conditions to exit the game
def events():
    for event in py.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            py.quit()
            sys.exit()


class Snake:
    def __init__(self):
        # Creates a starting direction movement and position
        self.direction = "right"
        self.x = CUBEWIDTH // 2
        self.y = CUBEHEIGHT // 2
        # TODO: change to 1 starting cube when 'apples' are implemented------------------
        # Creates an initial body with three cubes
        self.snakeBody = [{'x': self.x, 'y': self.y},
                          {'x': self.x - 1, 'y': self.y},
                          {'x': self.x - 2, 'y': self.y}]
        self.applePos = self.makeApple()
        self.score = 0

    # Moves the snake
    def movement(self):

        # Gets key press input
        move = py.key.get_pressed()

        # Changes the movement direction and prevents the user from moving back on themselves.
        if move[K_LEFT] and self.direction != "right":
            self.direction = "left"
        elif move[K_RIGHT] and self.direction != "left":
            self.direction = "right"
        elif move[K_UP] and self.direction != "down":
            self.direction = "up"
        elif move[K_DOWN] and self.direction != "up":
            self.direction = "down"

        # Returns true if no collisions occur.
        collisionFlag = self.collisionCheck()

        # Creates a new apple if the snakes head is at the same position as the apple
        if self.applePos['x'] == self.snakeBody[0]['x'] and self.applePos['y'] == self.snakeBody[0]['y']:
            self.applePos = self.makeApple()
            self.score += 1
        # Removes the tail (to be added back with each movement) if no apple was ate
        else:
            del self.snakeBody[-1]

        # Creates the new head position based on input movement
        if self.direction == "left":
            head = {'x': self.snakeBody[0]['x'] - 1, 'y': self.snakeBody[0]['y']}
        elif self.direction == "right":
            head = {'x': self.snakeBody[0]['x'] + 1, 'y': self.snakeBody[0]['y']}
        elif self.direction == "up":
            head = {'x': self.snakeBody[0]['x'], 'y': self.snakeBody[0]['y'] - 1}
        elif self.direction == "down":
            head = {'x': self.snakeBody[0]['x'], 'y': self.snakeBody[0]['y'] + 1}

        # Puts the direction based head position as the new head.
        self.snakeBody.insert(0, head)
        return collisionFlag

    # Checks for wall and self collisions
    def collisionCheck(self):
        # If the head (0 location in the list) hits any wall, game over.
        if self.snakeBody[0]['x'] == -1:
            return False
        elif self.snakeBody[0]['x'] == CUBEWIDTH:
            return False
        elif self.snakeBody[0]['y'] == -1:
            return False
        elif self.snakeBody[0]['y'] == CUBEHEIGHT:
            return False

        # If any x and y values of the body are the same as the head, game over.
        for cube in self.snakeBody[1:]:
            if self.snakeBody[0]['x'] == cube['x'] and self.snakeBody[0]['y'] == cube['y']:
                return False

        return True

    # Draws the snake after each movement check
    def drawSnake(self):
        # Gets the coordinates for each cube in the snake and draws them.
        for cube in self.snakeBody:
            x = cube['x'] * CUBESIZE
            y = cube['y'] * CUBESIZE
            py.draw.rect(WIN, BLACK, (x, y, CUBESIZE, CUBESIZE))

    # Assigns a location for an apple
    def makeApple(self):
        posCheck = True
        # Creates new apple positions until the apple does not occupy the same positions as the snake
        while True:
            possibleApple = {'x': random.randint(0, CUBEWIDTH - 1), 'y': random.randint(0, CUBEHEIGHT - 1)}
            for cube in range(len(self.snakeBody)):
                if possibleApple['x'] == self.snakeBody[cube]['x'] and possibleApple['y'] == self.snakeBody[cube]['y']:
                    posCheck = False

            if posCheck:
                break
            else:
                posCheck = True

        return possibleApple

    def drawApple(self):
        x = self.applePos['x'] * CUBESIZE
        y = self.applePos['y'] * CUBESIZE
        py.draw.rect(WIN, RED, (x, y, CUBESIZE, CUBESIZE))

    def drawScore(self):
        theScore = SCOREFONT.render('Score: %s' % (self.score), True, BLACK)
        scoreRect = theScore.get_rect()
        scoreRect.topright = (width, 0)
        WIN.blit(theScore, scoreRect)

    # Moves and draws the snake
    def do(self):
        # Returns true if no collisions occur.
        collisionFlag = self.movement()
        self.drawSnake()
        self.drawApple()
        self.drawScore()

        return collisionFlag


# Screen size
(width, height) = (600, 400)
WIN = py.display.set_mode((width, height))

# Colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 0)

# Size of each square (Must be divisible by width and height)
CUBESIZE = 20
# Gets the  number of cubes that can fit into the width and height to subdivide the window
CUBEWIDTH = int(width / CUBESIZE)
CUBEHEIGHT = int(height / CUBESIZE)


def Game():
    # Initializes game variables
    py.init()
    global SCOREFONT
    SCOREFONT = py.font.Font('freesansbold.ttf', 18)
    CLOCK = py.time.Clock()
    py.display.set_caption("Snake")
    FPS = 30

    S = Snake()

    running = True

    while running:
        # Delay between each re-draw
        py.time.delay(100)
        events()

        # Flag remains true until game over.
        keepPlaying = S.do()

        # If game over stop
        if not keepPlaying:
            running = False

        py.display.update()
        CLOCK.tick(FPS)
        WIN.fill(WHITE)


if __name__ == '__main__':
    Game()
    py.quit()
