from turtle import *

speed(0)
hideturtle()
for i in range (120):
    color('red')
    circle(i)
    color('orange')
    circle(i*0.4)
    right(3)
    forward(3)
done()