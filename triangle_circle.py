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
from turtle import TurtleScreen, RawTurtle

WIDTH = 2000
HEIGHT = 2000
diameter = 500
radius = int(diameter / 2)
# turtle.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg=None)

print(turtle.Screen().screensize(WIDTH, HEIGHT))
print(turtle.position())
turtle.Screen().setup(width=WIDTH, height=HEIGHT, startx=0, starty=0)
# print("height:", height)
# print("width:", width)
# yertle = Turtle(shape="turtle", visible=False)
# yertle.penup()

# creating turtle pen
t = turtle.Turtle()
t.penup()
t.hideturtle()
TURTLE_SIZE = 1

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT, startx=0, starty=0)
r = radius
t.goto(TURTLE_SIZE/2 - screen.window_width()/2 - 2*r, screen.window_height()/2 - TURTLE_SIZE/2 - r)
# t.pendown()
# t.showturtle()
t.speed('fastest')





# taking the input for the color
# col = input("Enter the color name or hex value of color(# RRGGBB): ")
# red hex "#FF0000"
col = "red"
t.pencolor(col)

# # set the fillcolor
t.fillcolor(col)

print("circle num:", int(screen.window_width()/(r)))
circle_num = int(screen.window_width()/(r))
for i in range(int(screen.window_height()/r)):
    for j in range(int(screen.window_width()/r)):

        t.begin_fill()
        t.circle(r)
        t.end_fill()
        t.forward(2*r)
        if j == circle_num - 1:
            if i % 2 == 0:
                print("even i:", i)
                print("even j:", j)
                t.backward(circle_num * 2 * r)
            else:
                print("odd i:", i)
                print("odd j:", j)
                t.backward((circle_num + 2) * 2 * r)
            # t.backward((circle_num + 2) * 2 * r)
            t.left(90)
            t.forward(r)
            t.right(90)
            t.forward(r)
            t.right(90)
            t.forward(math.sqrt(pow(2 * r, 2) - pow(r, 2)) + r)
            t.left(90)
            t.begin_fill()
            t.circle(r)
            t.end_fill()



ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")

turtle.exitonclick()
