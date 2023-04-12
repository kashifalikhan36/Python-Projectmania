from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=0
        self.penup
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"Level:- {self.level}",align="center",font=FONT)

    def level_increaser(self):
        self.level+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)