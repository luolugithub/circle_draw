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
point_contact = diameter / diameter
# Contact length is three point five-tenth of the diameter
line_contact = (diameter * 10) / diameter

print("point_contact:", point_contact)
print("line_contact:", line_contact)
# configuration for type of contact
distance_contact = line_contact

effective_circle = 0
rate_mian_kong = 0
# counter for point and line of contact
contact_line_counter = 0
contact_point_counter = 0
# contact shifting
shifting_contact = 20

if __name__ == '__main__':
    # six divided part axis
    A1_x = 0
    A1_y = 0
    A2_x = 0
    A2_y = 0
    A3_x = 0
    A3_y = 0
    for row in range(0, COUNT + 3, 1):
        for column in range(0, COUNT + 3, 1):
            # print("row:", row)
            # print("column:", column)
            # print("x:", x)
            # print("y:", y)
            cv2.circle(blank_image, center=(int(round(x, 6)), int(round(y, 6))), radius=radius,
                       color=(153, 102, 153, 255),
                       thickness=-1)

            # draw line on six parts of circle
            # https://zhidao.baidu.com/question/1643194553528453740.html
            # 1, (x+r,y)
            # 2, (x+radius*cos(2π/6),y+radius*sin(2π/6))
            # 3, (x+radius*cos(4π*/6),y+radius*sin(4π/6))
            # An (x+radius*cos(2π*(n-1)/n),y+radius*sin(2π*(n-1)/n))
            A1_x = int(x + radius - distance_contact)
            A1_y = int(y)
            A2_x = int(x + radius * math.cos(2 * math.pi / 6) - distance_contact)
            A2_y = int(y + radius * math.sin(2 * math.pi / 6))
            A3_x = int(x + radius * math.cos(4 * math.pi / 6) - distance_contact)
            A3_y = int(y + radius * math.sin(4 * math.pi / 6))

            if distance_contact == point_contact:
                shifting_contact = 20
            else:
                shifting_contact = 75
            cv2.line(img=blank_image, pt1=(A1_x, A1_y-shifting_contact), pt2=(A1_x, int(A1_y+shifting_contact)), color=(0, 0, 255, 255),
                     thickness=4)
            cv2.line(img=blank_image, pt1=(int(A2_x-shifting_contact*math.cos(150*math.pi/180.0)), int(A2_y-shifting_contact*math.sin(150*math.pi/180.0))), pt2=(int(A2_x+shifting_contact*math.cos(150*math.pi/180.0)), int(A2_y+shifting_contact*math.sin(150*math.pi/180.0))), color=(0, 255, 0, 255),
                     thickness=4)
            cv2.line(img=blank_image, pt1=(int(A3_x-shifting_contact*math.cos(30*math.pi/180.0)), int(A3_y-shifting_contact*math.sin(30*math.pi/180.0))), pt2=(int(A3_x+shifting_contact*math.cos(30*math.pi/180.0)), int(A3_y+shifting_contact*math.sin(30*math.pi/180.0))), color=(255, 0, 0, 255),
                     thickness=4)
            # print("A1_x:", A1_x)
            # print("A1_y:", A1_y)
            # print("A2_x:", A2_x)
            # print("A2_y:", A2_y)
            # print("A3_x:", A3_x)
            # print("A3_y:", A3_y)
            if (0 < A1_x < WIDTH) and (-radius < A1_y < HEIGHT):
                # point_type_counter
                if contact_line_counter < 60:
                    cv2.putText(img=blank_image, text=str(""), org=(A1_x, A1_y), color=(0, 0, 255, 0), thickness=8, fontFace=0, fontScale=1)
                    contact_line_counter = contact_line_counter + 1
                    cv2.putText(img=blank_image, text=str(""), org=(A2_x, A2_y), color=(0, 255, 0, 0), thickness=8, fontFace=0, fontScale=2)
                    contact_line_counter = contact_line_counter + 1
                    cv2.putText(img=blank_image, text=str(""), org=(A3_x, A3_y), color=(255, 0, 0, 0), thickness=8, fontFace=0, fontScale=2)
                    contact_line_counter = contact_line_counter + 1
                else:
                    distance_contact = point_contact
                    cv2.putText(img=blank_image, text=str(""), org=(A1_x, A1_y), color=(0, 0, 255, 0), thickness=8,
                                fontFace=0, fontScale=1)
                    contact_point_counter = contact_point_counter + 1
                    cv2.putText(img=blank_image, text=str(""), org=(A2_x, A2_y), color=(0, 255, 0, 0), thickness=8,
                                fontFace=0, fontScale=2)
                    contact_point_counter = contact_point_counter + 1
                    cv2.putText(img=blank_image, text=str(""), org=(A3_x, A3_y), color=(255, 0, 0, 0), thickness=8,
                                fontFace=0, fontScale=2)
                    contact_point_counter = contact_point_counter + 1
            print("distance_contact:", distance_contact)
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

    rate_mian_kong = (pixel_count - colors[0][1]) / pixel_count
    print("rate_mian_kong:", rate_mian_kong)

    cv2.imwrite('image/c500_strong_contact.png', blank_image)

    effective_circle = colors[0][1] / (math.pi * pow(radius, 2))
    print("effective_circle:", effective_circle)
    print("contact_line_counter:", contact_line_counter)
    print("contact_point_counter:", contact_point_counter)
