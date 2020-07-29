# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午4:52
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : tk_turtle.py
# @Software: PyCharm


import tkinter as tk
import turtle

root = tk.Tk()

canvas = turtle.ScrolledCanvas(root)
canvas.pack(side=tk.LEFT)

screen = turtle.TurtleScreen(canvas)
screen.setworldcoordinates(-10, 100, 100, -10)

turtle = turtle.RawTurtle(screen)
turtle.goto(90, 90)

screen.mainloop()