import turtle

turtle.Screen().bgcolor("Green")
turtle.Screen().setup(300, 400)
turtle.Screen().title("Welcome")
polygon = turtle.Turtle()

num_sides = 6
side_length = 70
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
