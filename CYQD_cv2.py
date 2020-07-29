# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 下午2:57
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : CYQD_cv2.py
# @Software: PyCharm

from PIL import Image, ImageDraw
import cv2
import numpy as np
import math

WIDTH = 2000
HEIGHT = 2000
diameter = 250
radius = int(diameter / 2)
x = 0
y = 0
COUNT = int(WIDTH / radius)
blank_image = np.zeros((HEIGHT, WIDTH, 4), np.uint8)
print("COUNT:", COUNT)
# Contact length is one-tenth of the diameter
# point_contact = (radius - math.sqrt(pow(radius, 2) - pow(radius/40, 2))) * 2
point_contact = diameter/100
# Contact length is three point five-tenth of the diameter
line_contact = (diameter * 3.5)/100

print("point_contact:", point_contact)
print("line_contact:", line_contact)
# configuration for type of contact
distance_contact = line_contact

if __name__ == '__main__':
    for row in range(0, COUNT + 3, 1):
        for column in range(0, COUNT + 3, 1):
            print("row:", row)
            print("column:", column)
            print("x:", x)
            print("y:", y)
            cv2.circle(blank_image, center=(int(round(x, 6)), int(round(y, 6))), radius=radius, color=(0, 0, 255, 255),
                       thickness=-1)
            x = x + diameter - distance_contact
            if column == COUNT:
                if row % 2 == 0:
                    x = - radius
                    y = y + math.sqrt(pow(diameter, 2) - pow(radius, 2)) - distance_contact
                else:
                    x = - diameter
                    y = y + math.sqrt(pow(diameter, 2) - pow(radius, 2)) - distance_contact

    cv2.imwrite('image/cyqd_line_contact.png', blank_image)
