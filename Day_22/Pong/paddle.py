from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        
        
    def path(self,path):
        self.goto(path, 0)

    def go_up(self):
        if self.ycor()<250:
            self.goto(self.xcor(), self.ycor()+20)
        else:
            pass

    def go_down(self):
        if self.ycor()>-250:
            self.goto(self.xcor(), self.ycor()-20)
        else:
            pass
