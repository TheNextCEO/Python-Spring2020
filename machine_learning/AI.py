import pygame
import random
import os
import time
import neat
# import visualize
import pickle

pygame.init()

width, height = 300, 540

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Flappy Bird")
bg_image = pygame.transform.scale(pygame.image.load("bg.png"),(width, height))

b_w, b_h = width//10, height//20
bird_imgs = [pygame.transform.scale(pygame.image.load("bird" + str(i) + ".png"), (b_w,b_h)) for i in range(1, 4)]

pipe_img = pygame.image.load(".pipe.png")

Clock = pygame.time.Clock()
# gen = 0
x = 40
y = 40


class Bg:
    def __init__(self):
        self.b1 = pygame.transform.scale(pygame.image.load("./bg.png"),(width, height))
        self.b2 = pygame.transform.scale(pygame.image.load("./bg.png"),(width, height))
        self.base1 = pygame.transform.scale(pygame.image.load("./base.png"),(width, height//20))
        self.base2 = pygame.transform.scale(pygame.image.load("./base.png"), (width, height // 20))
        self.v = width//40
        self.x = 0

    def show(self):
        screen.blit(self.b1, (self.x, 0))
        screen.blit(self.b2, (self.x + width, 0))
        _, h = self.base1.get_rect().size
        screen.blit(self.base1, (self.x, height - h))
        screen.blit(self.base2, (self.x + width, height - h))

    def move(self):
        self.x -= self.v
        if self.x <= -1*width:
            self.x = 0

    def stop(self):
        self.v = 0


class Bird:
    IMGS = bird_imgs

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.ALIVE_TIME = 0
        self.x, self.y = x, y
        self.tilt_angle = 0
        self.vy, self.vx, self.omega = 0, 0, 10
        self.g = 30
        self.dt = 0.1
        self.MAX_ANGLE, self.MIN_ANGLE = 45, -45
        self.start_time = self.ALIVE_TIME
        self.jump_vel = 50
        self.alive = True
        self.distance = 0
        self.image = None
        self.score = 0

    def show(self):
        Clock.tick(80)
        if self.tilt_angle <= self.MIN_ANGLE:
            img = 1
        else:
             img = self.ALIVE_TIME%3

        rotated_image = pygame.transform.rotate(self.IMGS[img], self.tilt_angle)
        new_rect = rotated_image.get_rect(center = self.IMGS[img].get_rect(topleft = (self.x,self.y) ).center)
        screen.blit(rotated_image, new_rect.topleft)

        self.mask = pygame.mask.from_surface(rotated_image)
        self.image = rotated_image

        if self.alive:
            self.ALIVE_TIME += 1
        else:
            self.tilt_angle = 0

    def click(self):
        if self.alive:
            self.vy = -1*self.jump_vel
            self.tilt_angle = self.MAX_ANGLE

    def move(self):
        if self.alive:
            self.distance += 1
            self.score += 3
            self.x += self.vx*self.dt
            self.y += self.dt*(self.vy + 0.5*self.g*self.dt)
            self.vy = self.vy + self.g* self.dt
            self.tilt_angle -= self.omega*self.dt

        if self.tilt_angle <= self.MIN_ANGLE:
            self.tilt_angle = self.MIN_ANGLE

    def groundCollision(self):
        if self.y <= height - height//20:
            return False
        else:
            self.alive = False
            return True

    def stop(self):
        # self.y = height - height//20 - height//20
        self.vy = 0
        self.vx = 0

        self.ALIVE_TIME = -1

    def getx(self):
        return self.x

    def getime(self):
        return self.ALIVE_TIME


class Pipes:
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.pipe_1 = pygame.transform.flip(pipe_img, False, True)
        self.pipe_2 = pipe_img
        self.v = width//40
        self.space = height//4
        self.y = height//7 + random.randint(0,height - self.space - height//20 - height//7 - height//9)


    def getx(self):
        return self.x

    def gety(self):
        return self.y, self.y + self.space


    def show(self):

        self.top = self.y

        self.pipe_1 = pygame.transform.scale(self.pipe_1, (int(b_w*(1.5)), self.y))
        screen.blit(self.pipe_1, (self.x, 0))
        yPos = height - self.space - self.y - height//20

        self.bottom = self.y + self.space
        self.pipe_2 = pygame.transform.scale(self.pipe_2, (int(b_w*(1.5)), yPos))
        screen.blit(self.pipe_2,(self.x, self.y + self.space))


    def passed(self):
        if self.x >= -1*b_w*1.5:
            return False
        return True

    def move(self):
        self.x -= self.v

    def stop(self):
        self.v = 0

def evalGenomes(genomes, config):
    # gen += 1

    Nnets = []
    birds = []
    ge = []

    for id, gene in genomes:
        gene.fitness = 0
        nnet = neat.nn.FeedForwardNetwork.create(gene, config)
        Nnets.append(nnet)
        birds.append(Bird(x, y))
        ge.append(gene)


# def main():
    playing = True
#     b = Bird(x, y)
    bg = Bg()
    DIST = 9*width//10
    pipes = [Pipes(5*width), Pipes(5*width + DIST)]

    score = 0

    while playing and len(birds) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                playing = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     b.click()

        # font = pygame.font.SysFont("comicsans", 18)
        # score = font.render('Score ' + str(b.score), True, (150, 150, 150), (255, 255, 255))
        ind = 0
        if len(pipes) > 1:
            if birds[0].x > pipes[0].x + pipes[0].pipe_1.get_width():
                ind = 1


        bg.show()
        for b in birds:
            b.show()
        for p in pipes:
            p.show()
        # screen.blit(score, (width - score.get_width() - 15, 10))

        for bird in birds:
            ge[birds.index(bird)].fitness += 0.1
            bird.move()

            # 0 -> dont click
            # 1 -> click
            activatedNodeVal = Nnets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[ind].top), abs(bird.y - pipes[ind].bottom)))

            if activatedNodeVal[0] > 0.5:
                bird.click()


        bg.move()
        for p in pipes:
            p.move()

        # check for pipe collision
        for b in birds:
            for p in pipes:
                if (0 <= b.y <= p.y or p.y + p.space <= b.y <= height) and p.x <= b.x <= p.x + 1.5*(b_w):
                    # bg.stop()
                    b.stop()
                    # pipes[0].stop()
                    # pipes[1].stop()
                    b.vx  = -5
                    b.vy = 0
                    ge[birds.index(b)].fitness -= 1
                    Nnets.pop(birds.index(b))
                    ge.pop(birds.index(b))
                    birds.pop(birds.index(b))
                    break
            # check for ground collision
            if b.groundCollision() or (b.y > height or b.y < 0):
                # bg.stop()
                b.stop()
                # for p in pipes:
                #     p.stop()
                b.g = 0
                b.vy = 0
                b.y = 19*height//20 - b_h

                ge[birds.index(b)].fitness -= 1
                Nnets.pop(birds.index(b))
                ge.pop(birds.index(b))
                birds.pop(birds.index(b))


        if pipes[0].passed():
            if not pipes[1].passed():
                pipes[0], pipes[1] = pipes[1], Pipes(pipes[1].getx() + DIST)
            else:
                pipes[0] = Pipes(b.getx() + width)
                pipes[1] = Pipes(pipes[0].getx() + DIST)

        pygame.display.update()


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

if __name__ == '__main__':

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
