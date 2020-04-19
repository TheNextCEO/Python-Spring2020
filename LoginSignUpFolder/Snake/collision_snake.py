# Snake by Daimeun Praytor

import sys, random
import pygame as py
from pygame.locals import *
import neat
import pickle
import os

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
            self.applePos = self.makeApple()
            self.score = 0

        # Moves the snake
        def movement(self,direction=0):
            global snakeSpeed
            # Gets key press input
            move = py.key.get_pressed()

            # Changes the movement direction and prevents the user from moving back on themselves.
            if direction == 2 and self.direction != "right":
                self.direction = "left"
            elif direction == 3 and self.direction != "left":
                self.direction = "right"
            elif direction == 0 and self.direction != "down":
                self.direction = "up"
            elif direction == 1 and self.direction != "up":
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
        gameOverSurf = GAMEOVERFONT.render('', True, BLACK)
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


    def evalGenomes(genomes, config):
        # Initializes game variables
        Nnets = []
        snakes = []
        ge = []

        for id, gene in genomes:
            gene.fitness = 0
            nnet = neat.nn.FeedForwardNetwork.create(gene, config)
            Nnets.append(nnet)
            snakes.append(Snake())
            ge.append(gene)

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

        while running and len(snakes) > 0:
            # Delay between each re-draw
            py.time.delay(snakeSpeed)
            exitGameCheck()

            # Flag remains true until game over.
            for S in snakes:
                print(len(snakes))
                sx = S.snakeBody[0]["x"]
                sy = S.snakeBody[0]["y"]
                ax = S.applePos["x"]
                ay = S.applePos["y"]
                distance = abs(sx - ax) + abs(sy - ay)
                dirx=-1
                diry=-1
                if sx<ax:
                    dirx=1
                if sy<ay:
                    diry=1

                val = Nnets[snakes.index((S))].activate((S.snakeBody[0]["x"], S.snakeBody[0]["y"], S.applePos["x"],
                                                         S.applePos["y"],distance,dirx,diry))


                if val[0] > 0.5:
                    # move snake vertically
                    S.movement(0)
                elif val[1] > 0.5:
                    # move snake down
                    S.movement(1)
                elif val[2] > 0.5:
                    # move snake left
                    S.movement(2)
                elif val[3] > 0.5:
                    # move snake right
                    S.movement(3)
                sx = S.snakeBody[0]["x"]
                sy = S.snakeBody[0]["y"]
                ax = S.applePos["x"]
                ay = S.applePos["y"]

                cur_distance = abs(sx - ax) + abs(sy - ay)

                if cur_distance < distance:
                    ge[snakes.index(S)].fitness += 0.1

                gameOver = S.do()
                # If game over, wait for a key to be pressed to restart
                if gameOver:
                    drawGameOver()
                    py.display.update()
                    # Wait for input allows the user to press any key to restart the game
                    # waitForInput()
                    ge[snakes.index(S)].fitness -= 0.1
                    ge.pop(snakes.index(S))
                    Nnets.pop(snakes.index(S))
                    snakes.pop(snakes.index(S))
                    S = Snake()
                    snakeSpeed = 100
                else:
                    ge[snakes.index(S)].fitness += 0.3


                py.display.update()
                CLOCK.tick(FPS)
                WIN.fill(WHITE)
    def run(config_file):
        config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                   neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                   config_file)

        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        # p.add_reporter(neat.Checkpointer(5))
        best = p.run(evalGenomes, 50)

        # show final stats
        print('\nBest genome:\n{!s}'.format(best))

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    print(config_path)
    run(config_path)