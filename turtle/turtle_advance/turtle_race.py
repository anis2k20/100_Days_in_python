from turtle import Turtle,Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colurs = ["blue","cyan","yellow","orange","red","purple","green"]
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will run the race? Enter a color: ")
print(user_bet)

y_position = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colurs[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner.")
            else:
                print(f"You've lose! The {winning_color} turtle is winner.")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
