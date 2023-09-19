from turtle import Turtle,Screen
import random
import turtle

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)
movement = ["left","right"]
directions = [0,90, 180, 270,]

"""
def draw_shape(num_of_side):
    angel = 360/num_of_side
    for _ in range(num_of_side):
        angel = 360/num_of_side
        tim.forward(100)
        tim.right(angel)

for shape_side_n in range(3,11):
    tim.color(random.choice(colurs))
    draw_shape(shape_side_n)

def left_right():
    direction = random.choice(movement)
    if direction == "left":
        left_move()
    elif direction == "right":
        right_move()

def left_move():
    tim.color(random.choice(colurs))
    tim.forward(20)
    tim.left(90)

def right_move():
    tim.color(random.choice(colurs))
    tim.forward(20)
    tim.right(90)
while True:
    left_right()

"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r,g,b)
    return random_color

tim.pensize(15)
for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick()