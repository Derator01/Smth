import turtle 

k = 30

turtle.left(90)
turtle.speed(100)

for i in range(4):
    turtle.forward(8*k)
    turtle.right(60)
    turtle.forward(8*k)
    turtle.right(120)

turtle.up()
turtle.speed(100)

for x in range(16,-10,-1):
    for y in range(13,-10,-1):
        turtle.goto(x*k, y*k)
        turtle.dot(3)

turtle.done()