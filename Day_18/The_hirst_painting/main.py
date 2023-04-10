import turtle as t
from random import choice, randint
import colorgram

colors = []
color = colorgram.extract("1.webp", 30)
for i in color:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    colors.append(new_color)
direction = [0, 90, 180, 270, 360]
timmy = t.Turtle()
t.colormode(255)
timmy.shape("circle")
timmy.width(20)
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
set()
k=timmy.ycor()
def set():
    timmy.goto(0,0)
    timmy.setheading(225)
    timmy.forward(250)
    timmy.setheading(0)
    
def move():
    timmy.color((choice(colors)))
    timmy.pendown()
    timmy.forward(1)
    timmy.penup()
    timmy.forward(50)
while True:
    set()
    timmy.goto(timmy.xcor(),k)
    k+=50
    for i in range(0,11):
        move()
    if k==500:
        break
    


screen = t.Screen()
screen.exitonclick()
