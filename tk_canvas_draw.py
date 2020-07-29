# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 上午9:03
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : tk_canvas_draw.py
# @Software: PyCharm


import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, background="black")
ysb = tk.Scrollbar(root, command=canvas.yview, orient="vertical")
xsb = tk.Scrollbar(root, command=canvas.xview, orient="horizontal")
canvas.configure(yscrollcommand=ysb.set, xscrollcommand=xsb.set)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

canvas.grid(row=0, column=0, sticky="nsew")
ysb.grid(row=0, column=1, sticky="ns")
xsb.grid(row=1, column=0, sticky="ew")

# designate that we want to draw in a 600x600 virtual canvas
canvas.configure(scrollregion=(0, 0, 599, 599))

canvas.create_line(0, 0, 599, 599, width=1, fill="white")
canvas.create_line(0, 599, 599, 0, width=1, fill="white")
canvas.create_rectangle(0, 0, 19, 19, fill="red")
canvas.create_rectangle(579, 579, 599, 599, fill="red")
canvas.create_rectangle(579, 0, 599, 19, fill="red")
canvas.create_rectangle(0, 579, 19, 599, fill="red")
canvas.create_rectangle(290, 290, 310, 310, fill="green")


root.mainloop()
