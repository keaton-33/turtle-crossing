from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed(0)
        self.penup()
        self.setposition(0, -340)
        self.setheading(90)

    def up(self):
        if self.ycor() < 340:
            self.forward(10)
