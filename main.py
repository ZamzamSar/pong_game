import turtle
from turtle import Turtle

wind = turtle.Screen() # creat screen to see the game

#creat address for the screen
wind.title('ping pong')

#creat back ground color and size the screen
wind.bgcolor('black') #color
wind.setup(width=800, height=600) #size
wind.tracer(0) #do not make update by her self

#racket1
racket1: Turtle =turtle.Turtle() #build first racket
racket1.speed(0) #if we want the speed fastest put 0
racket1.shape('square') #racket shape
racket1.color('blue') #racket color
racket1.penup() #F turtle drow line when moving F penup stop that
racket1.goto(-350, 0) #the left -400 , y =0
# the size for racket 1 20*20 pikel by  default
#if we want to chang the size
racket1.shapesize(stretch_wid=5, stretch_len=1)


#racket2
racket2 =turtle.Turtle() #build scound racket
racket2.speed(0) #if we want the speed fastest put 0
racket2.shape('square') #racket shape
racket2.color('green') #racket color
racket2.penup() #F turtle drow line when moving F penup stop that
racket2.goto(350, 0) #the right 400 , y =0
# the size for racket2 20*20 pikel by  default
#if we want to chang the size
racket2.shapesize(stretch_wid=5, stretch_len=1)


#ball
ball =turtle.Turtle() #build ball
ball.speed(0) #if we want the speed fastest put 0
ball.shape('square') #ball shape
ball.color('pink') #ball color
ball.penup() #F turtle drow line when moving F penup stop that
ball.goto(0, 0) #the midel 0 , y =0


#Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("player 1: 0 Player 2: 0", align="center", font=("Courier",24,"normal"))


#Functions
#racket1 move to up and down
def racket1_up():
    y = racket1.ycor()
    y +=20
    racket1.sety(y)

def racket1_down():
    y = racket1.ycor()
    y -=20
    racket1.sety(y)
#keyboard bindings
wind.listen() #there is keyboard press
wind.onkeypress(racket1_up, "w") #when press "w" it is racket1
wind.onkeypress(racket1_down, "s") #when press "w" it is racket1

#racket2
def racket2_up():
    y = racket2.ycor() #get y coordinate of R2
    y +=20
    racket2.sety(y) #set y of R2 to the new coordinate

def racket2_down():
    y = racket2.ycor()
    y -=20
    racket2.sety(y)
wind.onkeypress(racket2_up, "Up") #expect keyboard input
wind.onkeypress(racket2_down, "Down") #when press "w" it is racket2


#ball move
ball.dx = 2.5 #everytime the ball move increase y .3 (positive value move right and up)
ball.dy = 2.5


#main game loop
while True:
    wind.update() #updates the screen evrytime the loop run

    #move the ball
    ball.setx(ball.xcor() + ball.dx) #ball start 0 and everytime loop run --+.2
    ball.sety(ball.ycor() + ball.dy)
    #border check, top border +300px, bottom border -300px, ball is 20px
    #on the top and right
    if ball.ycor() >290: # if ball at top
        ball.sety(290) #set y coordinate +290
        ball.dy *= -1 #reverse direction , making +.2 ---> -.2
    #on bottom and right
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()> 390:
        ball.goto(0, 0)
        ball.dx*= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} Player 2: {}".format(score1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() <-390: #if ball at right
        ball.goto(0, 0) # return ball to center
        ball.dx *= -1
        score2 +=1
        score.clear()
    score.write("player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    #collision rackets and ball
    #Racket 1
    if (ball.xcor()> 340 and ball.xcor() < 350) and (ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1
    #Racket 2
    if (ball.xcor()< -340 and ball.xcor() > -350) and (ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
