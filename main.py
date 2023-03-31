from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(1280, 720)
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.bgcolor("gray")

player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.up, "Up")

# move_count and car_ready ensure multiple cars do not get placed in the same lane until the lane is clear (7 cycles)
car_ready = True
move_count = 0
car_list = []

# speed determines how long the game should sleep between each cycle. Is increased when user levels up
speed = 10
game_on = True
while game_on:
    screen.update()
    time.sleep(1 / speed)

    # Sets the list of available y-coordinates for generating cars then shuffles the list
    y_slots = [-300, -260, -220, -180, -140, -100, -60, -20, 20, 60, 100, 140, 180, 220, 260, 300]
    random.shuffle(y_slots)

    # Creates 0-3 cars in random y-coordinates from the y_slots list
    if car_ready:
        for n in range(random.randint(0, 3)):
            new_car = Car(y_slots.pop())
            car_list.append(new_car)
        car_ready = False

    # Moves all the cars in the car_list and detects if a car comes into contact with the player turtle
    for car in car_list:
        car.move()
        x = car.xcor()
        if -50 < x < 50:
            if abs(player.distance(0, car.ycor())) < 30:
                screen.update()
                game_on = False
                score.print_over()
                break
        # If car goes beyond -680, clears up the object and removes it from the car_list, then deletes the object
        elif x <= -680:
            car.clear()
            car.hideturtle()
            car_list.remove(car)
            del car

    # Enables new cars to be created after they have moved 70 units forward (to prevent overlapping or touching)
    move_count += 1
    if move_count == 7:
        car_ready = True
        move_count = 0

    # Detects if player has reached the opposite end, then resets the screen and increases the speed
    if player.ycor() == 340:
        speed += 5
        score.update_level()
        for car in car_list:
            car.clear()
            car.hideturtle()
            del car
        car_list = []
        player.setposition(0, -340)
        screen.update()
        time.sleep(1)


screen.exitonclick()
