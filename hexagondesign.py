
import turtle
turtle.bgcolor("black")
colors=['red','yellow','blue','green','cyan','purple']
turtle.speed(5)
for i in range(200):
    turtle.pencolor(colors[i%6])
    turtle.pensize(i/80 +1)
    turtle.forward(i)
    turtle.left(60)
turtle.Canvas()  