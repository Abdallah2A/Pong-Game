import random
import turtle

windows = turtle.Screen()
windows.title("Pong Game")
windows.bgcolor("gray")
windows.setup(width=800 ,height=600)
windows.tracer()

racket1 = turtle.Turtle()
racket1.shape("square")
racket1.color("dark red")
racket1.shapesize(stretch_wid=5 , stretch_len= 1)
racket1.penup()
racket1.speed(0)
racket1.goto(370  ,0)

racket2 = turtle.Turtle()
racket2.shape("square")
racket2.color("navy")
racket2.shapesize(stretch_wid=5 , stretch_len= 1)
racket2.penup()
racket2.speed(0)
racket2.goto(-370  ,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0  ,0)
ball.speed(0)
ball.dx = 20
ball.dy = random.randrange(-10, 10)

score1 = 0
score2 = 0 
score = turtle.Turtle()
score.speed(0)
score.color("dark green")
score.penup()
score.hideturtle()
score.goto(0 , 250)
score.write("0  :  0" ,align="center" ,font=("courier" ,20 ,"bold"))


def racket1_up():
    y = racket1.ycor()
    y += 40
    racket1.sety(y)


def racket1_down():
    y = racket1.ycor()
    y -= 40
    racket1.sety(y)


def racket2_up():
    y = racket2.ycor()
    y += 80
    racket2.sety(y)


def racket2_down():
    y = racket2.ycor()
    y -= 80
    racket2.sety(y)


windows.listen()
windows.onkeypress(racket1_up,"Up")
windows.onkeypress(racket1_down,"Down")
windows.onkeypress(racket2_up,"w")
windows.onkeypress(racket2_down,"s")


while True:
    windows.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if racket1.ycor() > 250:
        racket1.sety(250)
        
    if racket1.ycor() < -250:
        racket1.sety(-250)
        
    if racket2.ycor() > 250:
        racket2.sety(250)
        
    if racket2.ycor() < -250:
        racket2.sety(-250)
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        racket1.goto(370  ,0)
        racket2.goto(-370  ,0)
        ball.dy = random.randrange(-10,10)
        ball.dx *= -1
    
    if (ball.xcor() >= 350 and ball.xcor() <= 360) and (ball.ycor() <= racket1.ycor()+50 and ball.ycor() >= racket1.ycor()-50):
        ball.setx(350)
        ball.dy = random.randrange(-10 ,10)
        ball.dx *= -1
        
    if (ball.xcor() <= -350 and ball.xcor() >= -360) and (ball.ycor() <= racket2.ycor()+50 and ball.ycor() >= racket2.ycor()-50):
        ball.setx(-350)
        ball.dy = random.randrange(-10 ,10)
        ball.dx *= -1
        
    if (ball.xcor() >= 390):
        score1 += 1
        score.clear()
        score.write("{}  :  {}".format(score1, score2) ,align="center" ,font=("courier" ,20 ,"bold"))
        
    elif (ball.xcor() <= -390):
        score2 += 1
        score.clear()
        score.write("{}  :  {}".format(score1, score2)  ,align="center" ,font=("courier" ,20 ,"bold"))
        
    if score1 == 10:
        print("player 1 won")
        break
    
    if score2 == 10:
        print("Game Over loossser")
        break
