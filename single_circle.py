# -*- coding: utf-8 -*-
# @Time    : 2020/7/24 下午2:50
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : single_circle.py
# @Software: PyCharm


# draw color filled circle in turtle
import math
import turtle
import tkinter as tk
from turtle import Screen, Turtle
print(turtle.Screen().screensize())
print(turtle.position())
width, height = turtle.Screen().screensize()
print("height:", height)
print("width:", width)
# yertle = Turtle(shape="turtle", visible=False)
# yertle.penup()

# creating turtle pen
t = turtle.Turtle()
TURTLE_SIZE = 20

screen = Screen()
r = 60
t.penup()
t.goto(TURTLE_SIZE/2 - screen.window_width()/2 + r, screen.window_height()/2 - TURTLE_SIZE/2 - 2*r)
# t.pendown()
# t.showturtle()



# t.setup(canvwidth=2000, canvheight=2000, bg="black")
# taking input for the radius of the circle
# r = int(input("Enter the radius of the circle: "))
# r = 60

# taking the input for the color
# col = input("Enter the color name or hex value of color(# RRGGBB): ")
col = "blue"

# # set the fillcolor
# t.fillcolor(col)
#
# # start the filling color
# t.begin_fill()
#
# # drawing the circle of radius r
# t.circle(r)
#
# # ending the filling of the color
# t.end_fill()

for i in range(4):
    print("i:", i)
    t.circle(r)
    t.forward(2*r)
    t.circle(r)
    t.forward(2*r)
    t.circle(r)
    t.forward(2*r)
    t.circle(r)
    if i % 2 == 0:
        t.backward(8*r)
    else:
        t.backward(6*r)
    # t.backward(8*r)
    t.left(90)
    t.forward(r)
    t.right(90)
    t.forward(r)
    t.right(90)
    t.forward(math.sqrt(pow(2*r, 2) - pow(r, 2)) + r)
    t.left(90)
    t.circle(r)







ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")

turtle.exitonclick()
