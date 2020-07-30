# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 下午5:58
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : CYQD_Median.py
# @Software: PyCharm
import PIL
import cv2
import numpy as np
import math
import extcolors
from PIL import Image

WIDTH = 2000
HEIGHT = 2000
diameter = 500
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

effective_circle = 0
rate_mian_kong = 0

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

    img = Image.fromarray(blank_image)
    colors, pixel_count = extcolors.extract_from_image(img)
    print("colors:\n", colors)
    print("pixel_count:\n", pixel_count)

    rate_mian_kong = (pixel_count - colors[0][1])/pixel_count
    print("rate_mian_kong:", rate_mian_kong)

    cv2.imwrite('image/c500_median_contact.png', blank_image)

    effective_circle = colors[0][1]/(math.pi * pow(radius, 2))
    print("effective_circle:", effective_circle)

