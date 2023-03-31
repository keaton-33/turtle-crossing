from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setposition(-600, 330)
        self.color("black")
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(arg=f"Level {self.level}", align="left", font=("Arial", 18, "bold"))

    def print_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=("Arial", 48, "bold"))

    def update_level(self):
        self.level += 1
        self.print_level()
