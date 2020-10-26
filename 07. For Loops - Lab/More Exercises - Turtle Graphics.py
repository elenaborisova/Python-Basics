import turtle

my_turtle = turtle.Turtle()

# change the shape of the turtle
my_turtle.shape("turtle")
my_turtle.color("purple")

for i in range(0, 3):
    # draw a equilateral triangle
    my_turtle.left(30)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)

    # draw a line in the triangle
    my_turtle.left(-30)
    my_turtle.penup()
    my_turtle.backward(50)
    my_turtle.pendown()
    my_turtle.backward(100)
    my_turtle.penup()
    my_turtle.forward(150)
    my_turtle.pendown()
    my_turtle.left(30)

# hexagon
# for i in range(0, 6):
#     my_turtle.left(60)
#     my_turtle.forward(100)

turtle.done()