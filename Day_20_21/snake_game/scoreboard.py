from turtle import Turtle
ALIGNMENT="center"
FONT=("Arial",24,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over and Score: {self.score}",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()