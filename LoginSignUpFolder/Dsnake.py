# Snake by Daimeun Praytor

import sys, random
import pygame as py
from pygame.locals import *
from dbFolder.dbFunctions import nullEscDBClass as x

print(x.database.isLoggedIn())


if __name__ == '__main__':

    # Conditions to exit the game
    def exitGameCheck():
        for event in py.event.get():
            if event.type == QUIT:
                py.quit()
                sys.exit()


    # Returns when a key is pressed
    def waitForInput():
        while True:
            for event in py.event.get():
                if event.type == KEYDOWN:
                    return
                elif event.type == QUIT:
                    py.quit()
                    sys.exit()


    class Snake:
        def __init__(self):
            # Creates a starting direction movement and position
            self.direction = "right"
            self.x = CUBEWIDTH // 2
            self.y = CUBEHEIGHT // 2
            # TODO: change to 1 starti-------------ng cube when 'apples' are implemented-----
            # Creates an initial body with three cubes
            self.snakeBody = [{'x': self.x, 'y': self.y},
                              {'x': self.x - 1, 'y': self.y},
                              {'x': self.x - 2, 'y': self.y}]
            self.applePos = self.makeApple()
            self.score = 0

        # Moves the snake
        def movement(self):
            global snakeSpeed
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
                # Makes the snake go faster for every apple eaten
                if snakeSpeed >= 50:
                    snakeSpeed -= 2
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
            x = self.snakeBody[0]['x'] * CUBESIZE
            y = self.snakeBody[0]['y'] * CUBESIZE
            py.draw.rect(WIN, BLUE, (x, y, CUBESIZE, CUBESIZE))

            # TODO Scale math for the eyes (Instead of CUBESIZE - 7)
            if self.direction == "left":
                py.draw.rect(WIN, BLACK, (x + 3, y + 3, CUBESIZE // 4, CUBESIZE // 4))
                py.draw.rect(WIN, BLACK, (x + 3, y + CUBESIZE - 7, CUBESIZE // 4, CUBESIZE // 4))
            elif self.direction == "right":
                py.draw.rect(WIN, BLACK, (x + CUBESIZE - 7, y + 3, CUBESIZE // 4, CUBESIZE // 4))
                py.draw.rect(WIN, BLACK, (x + CUBESIZE - 7, y + CUBESIZE - 7, CUBESIZE // 4, CUBESIZE // 4))
            elif self.direction == "up":
                py.draw.rect(WIN, BLACK, (x + 3, y + 3, CUBESIZE // 4, CUBESIZE // 4))
                py.draw.rect(WIN, BLACK, (x + CUBESIZE - 7, y + 3, CUBESIZE // 4, CUBESIZE // 4))
            elif self.direction == "down":
                py.draw.rect(WIN, BLACK, (x + 3, y + CUBESIZE - 7, CUBESIZE // 4, CUBESIZE // 4))
                py.draw.rect(WIN, BLACK, (x + CUBESIZE - 7, y + CUBESIZE - 7, CUBESIZE // 4, CUBESIZE // 4))

            # Gets the coordinates for each cube in the snake and draws them.
            counter = 1
            for cube in self.snakeBody[1:]:
                x = cube['x'] * CUBESIZE
                y = cube['y'] * CUBESIZE
                if counter % 2 == 1:
                    py.draw.rect(WIN, BLACK, (x, y, CUBESIZE, CUBESIZE))
                else:
                    py.draw.rect(WIN, BLUE, (x, y, CUBESIZE, CUBESIZE))
                counter += 1

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
            scoreSurf = SCOREFONT.render('Score: %s' % (self.score), True, BLACK)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topright = (width, 0)
            WIN.blit(scoreSurf, scoreRect)

        # Moves and draws the snake
        def do(self):
            # Returns true if no collisions occur.
            collisionFlag = self.movement()
            self.drawSnake()
            self.drawApple()
            self.drawScore()

            return collisionFlag


    def drawGameOver():
        gameOverSurf = GAMEOVERFONT.render('GAME OVER', True, BLACK)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (width // 2, height // 2)
        WIN.blit(gameOverSurf, gameOverRect)


    # Screen size
    (width, height) = (600, 400)
    WIN = py.display.set_mode((width, height))

    # Colors
    BLACK = (0, 0, 0, 255)
    GREEN = (0, 255, 0, 0)
    BLUE = (0, 0, 255, 0)
    WHITE = (255, 255, 255, 255)
    RED = (255, 0, 0, 0)

    # Size of each square (Must be divisible by width and height)
    CUBESIZE = 10
    # Gets the  number of cubes that can fit into the width and height to subdivide the window
    CUBEWIDTH = int(width / CUBESIZE)
    CUBEHEIGHT = int(height / CUBESIZE)

    snakeSpeed = 100


    def Game():
        # Initializes game variables
        py.init()
        global snakeSpeed

        global SCOREFONT
        global GAMEOVERFONT

        SCOREFONT = py.font.Font('slkscr.ttf', 18)
        GAMEOVERFONT = py.font.Font('slkscrb.ttf', 36)
        CLOCK = py.time.Clock()
        py.display.set_caption("Snake")
        FPS = 60

        S = Snake()

        running = True

        while running:
            # Delay between each re-draw
            py.time.delay(snakeSpeed)
            exitGameCheck()

            # Flag remains true until game over.
            keepPlaying = S.do()

            # If game over, wait for a key to be pressed to restart
            if not keepPlaying:
                drawGameOver()
                py.display.update()
                database.saveScore("snake", int(S.score))
                snakeSpeed = 100
                waitForInput()
                del S
                S = Snake()

            py.display.update()
            CLOCK.tick(FPS)
            WIN.fill(WHITE)
        #print(int(S.score))
        #database.saveScore("snake", int(S.score))
    Game()
    py.quit()
