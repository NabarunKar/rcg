import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.left(90)
        self.left(90)
        self.a = random.randint(-300,300)
        self.goto(300, self.a)

    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
