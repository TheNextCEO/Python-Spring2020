import turtle
wn=turtle.Screen()
wn.title("Pong game")
wn.bgpic("source.gif")
wn.update()
wn.setup(width=800,height=600)
wn.tracer(0)

#score
score_a=0
score_b=0
#paddle A
paddle_a = turtle.Turtle()  #tutle object
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#hey
#testing
#changing
#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=0.2   #each time you move it moves 2 pixels
ball.dy=-0.2


#pen for scoring

pen = turtle.Turtle()
pen.speed(0)  #animation speed not movement
pen.color("white")
pen.penup()  #to not to see a line moving
pen.hideturtle() #cause we dont want to see it
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center",font=("Courier",20,"normal"))

#Functions to move paddles

def paddle_a_up():
    y=paddle_a.ycor()
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -=20
    paddle_b.sety(y)

#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"Up")
wn.onkeypress(paddle_a_down,"Down")
wn.onkeypress(paddle_b_up,"q")
wn.onkeypress(paddle_b_down,"r")

#LOOP
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1  #moves back or down each time it reaches the height

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))

    #paddle and ball collisions
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

