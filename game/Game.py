import pygame
import os


class player:
    pass

def game():
    pygame.init()

    # width and height of the screen
    width = 960
    height = 500


    w = 10
    h = 10

    # initial x and y coordinates
    x = 100
    y = 481

    # default x and y velocities
    vel_x = 2
    vel_y = -3

    # constant y and acceleration
    v_y = -3
    a = 0.1

    # setting the screen
    screen = pygame.display.set_mode((width, height))
    # setting the caption of the image
    pygame.display.set_caption("Null Escape")

    # image height
    img_h = 120

    # setting the image
    img = pygame.transform.scale(pygame.image.load("player.png"), (50,50))
    bg1 = pygame.transform.scale(pygame.image.load("bg.png"), (width, height))
    bg2 = pygame.transform.scale(pygame.image.load("bg.png"), (width, height))
    # variable to run
    run = True

    # variable to store the time
    t = 0
    up_pressed = False

    # Game loop
    while run:
        pygame.display.update()
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel_x
        if keys[pygame.K_RIGHT]:
            x += vel_x

        if keys[pygame.K_UP]:
            if up_pressed == False:
                t = 0
                up_pressed = True
                y_0 = y

        if up_pressed == True:

            t += 1
            y = y_0 + v_y*t + 0.5*a*t*t

            if y >= height:
                t = 0
                y = height - 10
                up_pressed = False
                vel_y = v_y

        if keys[pygame.K_DOWN]:
            y += vel_y

        screen.fill((0,0,0))
        screen.blit(bg1, (0,0))
        screen.blit(img, (x,y - img_h))

        pygame.display.update()

    pygame.quit()
    return


if __name__ == "__main__":
    game()