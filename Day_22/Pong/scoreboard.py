from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",40,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.penup
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.r_score,align=ALIGNMENT,font=FONT)
        self.goto(100,250)
        self.write(self.l_score,align=ALIGNMENT,font=FONT)

    def l_score_increase(self):
        self.l_score+=1
        self.update_scoreboard()
    def r_score_increase(self):
        self.r_score+=1
        self.update_scoreboard()