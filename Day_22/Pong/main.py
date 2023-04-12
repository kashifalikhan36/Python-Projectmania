from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
screen=Screen()
paddle_1=Paddle()
paddle_2=Paddle()
ball=Ball()
scoreboard=ScoreBoard()

screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

paddle_1.path(380)
paddle_2.path(-380)

screen.listen()
screen.onkeypress(paddle_1.go_up,"Up")
screen.onkeypress(paddle_1.go_down,"Down")
screen.onkeypress(paddle_2.go_up,"w")
screen.onkeypress(paddle_2.go_down,"s")

is_game_on=True
while is_game_on:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()

    if ball.distance(paddle_1)<30 or ball.distance(paddle_2)<30:
        ball.ball_speed*=0.9
        ball.bounce_x()

    if ball.xcor()>400:
        scoreboard.r_score_increase()
        ball.reset_position()
        
    elif ball.xcor()<-400:
        scoreboard.l_score_increase()
        ball.reset_position()

screen.exitonclick()