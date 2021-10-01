import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 5)
        if chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            pos = random.randint(-250, 280)
            car.goto(300, pos)
            self.cars.append(car)

    def move(self):
        for i in self.cars:
            i.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT
