import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

cars_store = []

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

screen.listen()
screen.onkeypress(player.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move()
    for car in car_manager.new_cars:

        if player.distance(car) < 12:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() >= 290:
        scoreboard.level_increaser()
        player.start()
        car_manager.speed_inc()
screen.exitonclick()
