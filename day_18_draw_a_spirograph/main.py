import turtle
import random

zolwik = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color


zolwik.pensize(2)
zolwik.speed("fastest")

def draw_spirograph(size_of_gap):

    for _ in range(int(360/size_of_gap)):
        direction = zolwik.heading()
        zolwik.color(random_color())
        zolwik.circle(100)
        zolwik.setheading(direction + size_of_gap)

draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
