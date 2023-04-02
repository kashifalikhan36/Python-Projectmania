from turtle import Turtle, Screen
import random
turtles=["yellow","green","blue","orange","red","black"]
real_turtles=[]
screen=Screen()
user_bet=screen.textinput("Makke ur bet","Which turtle will wn the race? Enter a color:")
k=0
p=-100
for i in range(0,6):
    print(i)
    d=Turtle()
    d.shape("turtle")
    d.color(turtles[k])
    d.penup()
    d.goto(-230,p)
    k+=1
    p+=50
    real_turtles.append(d)
is_true=True
while is_true:
    for turtle in real_turtles:
        if turtle.xcor()>230:
            win=turtle.pencolor()
            if win==user_bet:
                print(f"You've won! the {win} turtle is the winner!")
                is_true=False
            else:
                print(f"You've loss! the {win} turtle is the winner!")
                is_true=False
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()