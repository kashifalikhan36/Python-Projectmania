from turtle import Turtle
import random

DIRECTION=[0,45,90,180,270,360]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed=0.1
        self.shape("circle")
        self.color('white')
        self.speed("slowest")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.shapesize(0.7,0.7)

    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *=-1
    def bounce_x(self):
        self.x_move *=-1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()