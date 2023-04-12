from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.speed=0.1
        self.new_cars=[]

    def create_cars(self):
        random_chance=random.randint(0,6)
        if random_chance==1:
            new_car=Turtle()
            new_car.start_distance=STARTING_MOVE_DISTANCE
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(1,2)
            new_car.goto(280,random.randrange(-280,280))
            self.new_cars.append(new_car)
    
    def move(self):
        for car in self.new_cars:
            car.fd(STARTING_MOVE_DISTANCE)
    
    def speed_inc(self):
        self.speed*=0.9