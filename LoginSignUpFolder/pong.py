"""
import pygame

pygame.init()

size=width,height=500,500
speed=[2,2]
black=0,0,0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pong Game")
ball = pygame.draw.rect(screen,(255,0,0),5,5)
ballrect=ball.get_rect()
run = True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] =-speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(black)
    screen.blit(ball,ballrect)
    pygame.display.flip()
pygame.quit()
"""

import turtle

class pongGame(object):

    def setuppong(self):
        self.wn=turtle.Screen()
        self.wn.title("Pong game")
        self.wn.bgpic("source.gif")
        self.wn.update()
        self.wn.setup(width=800,height=600)
        self.wn.tracer(0)

        #score
        self.score_a=0
        self.score_b=0

        #paddle A
        self.paddle_a = turtle.Turtle()  #tutle object
        self.paddle_a.speed(0)
        self.paddle_a.shape("square")
        self.paddle_a.color("white")
        self.paddle_a.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_a.penup()
        self.paddle_a.goto(-350,0)

        #paddle B
        self.paddle_b = turtle.Turtle()
        self.paddle_b.speed(0)
        self.paddle_b.shape("square")
        self.paddle_b.color("white")
        self.paddle_b.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle_b.penup()
        self.paddle_b.goto(350,0)

        #ball
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0,0)
        self.ball.dx=3.5   #each time you move it moves 2 pixels
        self.ball.dy=-3.5

        #pen for scoring
        self.pen = turtle.Turtle()
        self.pen.speed(0)  #animation speed not movement
        self.pen.color("white")
        self.pen.penup()  #to not to see a line moving
        self.pen.hideturtle() #cause we dont want to see it
        self.pen.goto(0,260)
        self.pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",20,"normal"))

        # keyboard binding
        self.wn.listen()
        self.wn.onkeypress(self.paddle_a_up, "Up")
        self.wn.onkeypress(self.paddle_a_down, "Down")
        self.wn.onkeypress(self.paddle_b_up, "q")
        self.wn.onkeypress(self.paddle_b_down, "r")

    #Functions to move paddles
    def paddle_a_up(self):
        y = self.paddle_a.ycor()
        y += 20
        self.paddle_a.sety

    def paddle_a_down(self):
        y = self.paddle_a.ycor()
        y -= 20
        self.paddle_a.sety

    def paddle_b_up(self):
        y = self.paddle_b.ycor()
        y += 20
        self.paddle_b.sety

    def paddle_b_down(self):
        y = self.paddle_b.ycor()
        y -= 20
        self.paddle_b.sety


    #LOOP
    def start(self):
        bool1 = True
        while bool1:
            self.wn.update()

            #move the ball
            self.ball.setx(self.ball.xcor()+self.ball.dx)
            self.ball.sety(self.ball.ycor()+self.ball.dy)

            #border checking
            if self.ball.ycor()>290:
                self.ball.sety(290)
                self.ball.dy*=-1  #moves back or down each time it reaches the height

            if self.ball.ycor()<-290:
                self.ball.sety(-290)
                self.ball.dy*=-1

            if self.ball.xcor() >390:
                self.ball.goto(0,0)
                self.ball.dx *=-1
                self.score_a +=1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {}".format(self.score_a,self.score_b), align="center", font=("Courier", 20, "normal"))

            if self.ball.xcor() < -390:
                self.ball.goto(0, 0)
                self.ball.dx *= -1
                self.score_b +=1
                self.pen.clear()
                self.pen.write("Player A: {} Player B: {}".format(self.score_a,self.score_b), align="center", font=("Courier", 20, "normal"))

            #paddle and ball collisions
            if self.ball.xcor()>340 and self.ball.xcor()<350 and (self.ball.ycor()<self.paddle_b.ycor()+40 and self.ball.ycor()>self.paddle_b.ycor()-40):
                self.ball.setx(340)
                self.ball.dx *= -1

            if self.ball.xcor()<-340 and self.ball.xcor()>-350 and (self.ball.ycor()<self.paddle_a.ycor()+40 and self.ball.ycor()>self.paddle_a.ycor()-40):
                self.ball.setx(-340)
                self.ball.dx *= -1


if "_name_" == "__main__":
    x = pongGame()
    x.setuppong()
    x.start()