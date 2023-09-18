import colorgram, turtle, random

color_list = [(7, 25, 6), (102, 97, 65), (2, 7, 11), (44, 43, 16), (67, 91, 12), (133, 167, 32), (180, 159, 121),
              (87, 118, 71), (105, 83, 97), (45, 29, 36), (133, 155, 184), (45, 90, 13), (82, 97, 122), (136, 154, 142),
              (173, 139, 167), (229, 209, 185), (93, 50, 43), (107, 149, 83), (201, 216, 239), (207, 209, 120),
              (79, 54, 64), (154, 110, 141), (111, 118, 169), (174, 108, 92), (204, 234, 222), (177, 177, 229),
              (233, 211, 228), (198, 218, 11), (214, 171, 213), (56, 58, 84)]

zolwik = turtle.Turtle()
turtle.colormode(255)
zolwik.speed(10)
number_of_dots = 100

zolwik.penup()
zolwik.setheading(225)
zolwik.forward(400)
zolwik.setheading(0)
zolwik.pendown()

for dot in range(1, number_of_dots + 1):
    zolwik.dot(20, random.choice(color_list))
    zolwik.penup()
    zolwik.forward(50)
    zolwik.pendown()
    if dot % 10 == 0:
        zolwik.left(90)
        zolwik.penup()
        zolwik.forward(50)
        zolwik.pendown()
        zolwik.left(90)
        zolwik.penup()
        zolwik.forward(500)
        zolwik.pendown()
        zolwik.setheading(0)

# rgb_colours = []
# colors = colorgram.extract('picture_1.jpg',30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colours.append((r,g,b))
# print(rgb_colours)

screen = turtle.Screen()
screen.exitonclick()
