from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Car(Turtle):
    def __init__(self, ycor):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.turtlesize(1.5, 3)
        self.speed(0)
        self.penup()
        self.setheading(180)
        self.setposition(680, ycor)

    def move(self):
        if self.xcor() > -680:
            self.forward(10)

