# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 下午4:52
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : tk_turtle.py
# @Software: PyCharm


import tkinter as tk
import turtle

root = tk.Tk()
canvas = turtle.Canvas(root, width=2000, height=2000)
# canvas = turtle.ScrolledCanvas(root)
canvas.pack(side=tk.LEFT)


screen = turtle.TurtleScreen(canvas)

# screen.setworldcoordinates(0, 0, 2000, 2000)

turtle = turtle.RawTurtle(screen)
turtle.goto(0, 0)

screen.mainloop()