import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(player.move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    # collision
    for i in car_manager.cars:
        if player.distance(i) < 22:
            scoreboard.game_over()
            game_is_on = False
    # detecting cross
    if player.has_crossed():
        player.reset()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()
