# Snake by Daimeun Praytor

import sys, random
import pygame as py
from pygame.locals import *
from dbFolder.dbFunctions import nullEscDBClass

db = nullEscDBClass()
db.startGameCon()
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

            # Creates an initial body with three cubes
            self.snakeBody = [{'x': self.x, 'y': self.y},
                              {'x': self.x - 1, 'y': self.y},
                              {'x': self.x - 2, 'y': self.y}]
            self.appleCount = 0
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

            # Checks for self collision (Game over) and wall collision (wrap snake)
            collisionFlag = self.selfCollision()
            wallFlag = self.wallCollision()

            foundApple = False
            # Creates a new apple if the snakes head is at the same position as the apple
            for appleIndex in self.applePos:
                if appleIndex['x'] == self.snakeBody[0]['x'] and appleIndex['y'] == self.snakeBody[0]['y']:
                    # Makes the snake go faster for every apple eaten
                    # Does not go lower than a 50ms delay
                    if snakeSpeed >= 50:
                        snakeSpeed -= 2

                    # Deletes the apple that was ate and adjusts variables to reflect the change.
                    self.applePos.remove(appleIndex)
                    foundApple = True
                    self.appleCount -= 1
                    self.applePos = self.makeApple()
                    self.score += 1

            # Removes the tail (to be added back with each movement) if no apple was ate
            if not foundApple:
                del self.snakeBody[-1]

            # Creates the new head position based on input movement
            # If there is a wall collision, move snake to opposite side of screen
            if wallFlag:
                if self.direction == "left":
                    head = {'x': CUBEWIDTH - 1, 'y': self.snakeBody[0]['y']}
                elif self.direction == "right":
                    head = {'x': 0, 'y': self.snakeBody[0]['y']}
                elif self.direction == "up":
                    head = {'x': self.snakeBody[0]['x'], 'y': CUBEHEIGHT - 1}
                elif self.direction == "down":
                    head = {'x': self.snakeBody[0]['x'], 'y': 0}
            else:
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
        def selfCollision(self):
            # If any x and y values of the body are the same as the head, game over.
            for cube in self.snakeBody[1:]:
                if self.snakeBody[0]['x'] == cube['x'] and self.snakeBody[0]['y'] == cube['y']:
                    return True

            return False

        # This detects if the head hits a wall
        def wallCollision(self):
            # If the head (0 location in the list) hits any wall, change head position to opposite wall.
            if self.snakeBody[0]['x'] == 0 and self.direction == "left":
                return True
            elif self.snakeBody[0]['x'] == CUBEWIDTH-1 and self.direction == "right":
                return True
            elif self.snakeBody[0]['y'] == 0 and self.direction == "up":
                return True
            elif self.snakeBody[0]['y'] == CUBEHEIGHT-1 and self.direction == "down":
                return True

            return False

        # Draws the snake after each movement check
        def drawSnake(self):
            x = self.snakeBody[0]['x'] * CUBESIZE
            y = self.snakeBody[0]['y'] * CUBESIZE
            py.draw.rect(WIN, BLUE, (x, y, CUBESIZE, CUBESIZE))

            # This displays the eyes based on the current direction of the snake
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

                # Alternates color of each section of the snake
                if counter % 2 == 1:
                    py.draw.rect(WIN, BLACK, (x, y, CUBESIZE, CUBESIZE))
                else:
                    py.draw.rect(WIN, BLUE, (x, y, CUBESIZE, CUBESIZE))
                counter += 1

        # Assigns a location for an apple
        # If there are no apples, create a new apple
        # There is a 10% chance to get 5 apples.
        def makeApple(self):
            if self.appleCount == 0:
                # Stores the apples
                appleList = []
                # Used for a 10% chance
                appleRNG = random.randint(1, 10)

                # 90% of the time only one apple is made
                if appleRNG > 1:
                    posCheck = True
                    # Creates new apple positions until the apple does not occupy the same positions as the snake
                    while True:
                        possibleApple = {'x': random.randint(0, CUBEWIDTH - 1), 'y': random.randint(0, CUBEHEIGHT - 1)}
                        for cube in range(len(self.snakeBody)):
                            if possibleApple['x'] == self.snakeBody[cube]['x'] and possibleApple['y'] == self.snakeBody[cube]['y']:
                                posCheck = False

                        # If the apple position is not on a snake body part, add the apple to the game.
                        if posCheck:
                            appleList.append(possibleApple)
                            self.appleCount += 1
                            return appleList
                        else:
                            posCheck = True

                # 10% chance to create 5 purple apples
                else:
                    posCheck = True
                    # Creates new apple positions until the apple does not occupy the same positions as the snake
                    while self.appleCount < 5:
                        possibleApple = {'x': random.randint(0, CUBEWIDTH - 1), 'y': random.randint(0, CUBEHEIGHT - 1)}
                        for cube in range(len(self.snakeBody)):
                            if possibleApple['x'] == self.snakeBody[cube]['x'] and possibleApple['y'] == self.snakeBody[cube]['y']:
                                posCheck = False

                        # If the apple position is not on a snake body part, add the apple to the game.
                        if posCheck:
                            appleList.append(possibleApple)
                            self.appleCount += 1
                        else:
                            posCheck = True
                    return appleList

            # If no new apples were made return the original apple positions
            else:
                return self.applePos

        # Draws the apple on the screen based on the x,y positions
        def drawApple(self):
            for apple in self.applePos:
                x = apple['x'] * CUBESIZE
                y = apple['y'] * CUBESIZE

                # If there is more than one apple color them purple
                if self.appleCount == 1:
                    py.draw.rect(WIN, RED, (x, y, CUBESIZE, CUBESIZE))
                else:
                    py.draw.rect(WIN, PURPLE, (x, y, CUBESIZE, CUBESIZE))

        # Draws the score on the screen
        def drawScore(self):
            scoreSurf = SCOREFONT.render('Score: %s' % (self.score), True, BLACK)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topright = (width, 0)
            WIN.blit(scoreSurf, scoreRect)

        # Moves and draws the snake, apple, and score.
        def do(self):
            # Returns true if collisions occur.
            collisionFlag = self.movement()
            self.drawSnake()
            self.drawApple()
            self.drawScore()

            # If collision flag is true, game over.
            return collisionFlag

    # Draws game over message to the screen
    def drawGameOver():
        gameOverSurf = GAMEOVERFONT.render('GAME OVER', True, BLACK)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (width//2, height//2)
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
    PURPLE = (121, 7, 242, 1)

    # Size of each square (Must be divisible by width and height)
    CUBESIZE = 20

    # Gets the  number of cubes that can fit into the width and height to subdivide the window
    CUBEWIDTH = int(width / CUBESIZE)
    CUBEHEIGHT = int(height / CUBESIZE)

    # Keeps track of the snake speed, this is a delay between frames.
    # A lower number is faster.
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

        # Main game loop
        while running:
            # Delay between each re-draw
            py.time.delay(snakeSpeed)
            exitGameCheck()

            # Flag remains true until game over.
            gameOver = S.do()

            # If game over, wait for a key to be pressed to restart
            if gameOver:
                drawGameOver()
                py.display.update()

                # Saves the current users score to the highscores with their information
                db.saveScore("Snake", S.score)

                # Wait for input allows the user to press any key to restart the game
                waitForInput()

                # Resets the snake object and the speed variable to get ready for the next game.
                del S
                S = Snake()
                snakeSpeed = 100

            py.display.update()
            CLOCK.tick(FPS)
            WIN.fill(WHITE)

    Game()
    py.quit()
