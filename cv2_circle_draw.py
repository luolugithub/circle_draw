# -*- coding: utf-8 -*-
# @Time    : 2020/7/29 上午9:44
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : cv2_circle_draw.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 上午9:19
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : pillow_draw.py
# @Software: PyCharm


from PIL import Image, ImageDraw
import cv2
import numpy as np
import math

WIDTH = 2000
HEIGHT = 2000
R = 250
x = 0
y = 0
COUNT = int(WIDTH/R)
blank_image = np.zeros((HEIGHT, WIDTH, 4), np.uint8)
# cv2.circle(blank_image, center=(x, y), radius=int(R / 2), color=(0, 0, 255, 255), thickness=-1)
# cv2.circle(blank_image, center=(x + R, y), radius=int(R / 2), color=(0, 0, 255, 255), thickness=-1)
print("COUNT:", COUNT)
for row in range(0, COUNT + 3, 1):
    for column in range(0, COUNT + 3, 1):
        print("row:", row)
        print("column:", column)
        print("x:", x)
        print("y:", y)
        cv2.circle(blank_image, center=(int(round(x, 6)), int(round(y, 6))), radius=int(R / 2), color=(0, 0, 255, 255), thickness=-1)
        x = x + R
        if column == COUNT:
            if row % 2 == 0:
                x = - R/2
                y = y + math.sqrt(pow(R, 2) - pow(R/2, 2))
            else:
                x = - R
                y = y + math.sqrt(pow(R, 2) - pow(R / 2, 2))






# im.show()
cv2.imwrite('image/cv2_imagedraw.png', blank_image)
