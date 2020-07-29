# -*- coding: utf-8 -*-
# @Time    : 2020/7/28 上午9:19
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : pillow_draw.py
# @Software: PyCharm


from PIL import Image, ImageDraw
import cv2
import numpy as np

WIDTH = 2000
HEIGHT = 2000
R = 500
start_x = -500
start_y = -500
x1 = -500
y1 = -500
x2 = 500
y2 = 500

im = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0, 0))
draw = ImageDraw.Draw(im)

blank_image = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
cv2.circle(blank_image, center=(0, 0), radius=int(R / 2), color=(0, 0, 255), thickness=-1)
# draw.ellipse((x1, y1, x2, y2), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
# draw.ellipse((x1 + 2*R, y1, x2 + 2*R, y2), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
# draw.ellipse((x1 + 4*R, y1, x2 + 4*R, y2), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
# # draw.ellipse((x1, y1 + 2*R, x2, y2 + 2*R), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
# draw.ellipse((x1 + R, y1 + 2*R, x2 + R, y2 + 2*R), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))

# print("int(WIDTH/R):", int(WIDTH/R))
# for w_num in range(int(WIDTH/R)):
#     for h_num in range(int(HEIGHT/R)):
#         print("w_num:", w_num)
#         print("h_num:", h_num)
#         print("start_x:", start_x)
#         print("start_y:", start_y)
#         # draw.ellipse((x1, y1, x2, y2), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
#         if h_num < (int(WIDTH/R)):
#             draw.ellipse((x1 + h_num*R, y1, x2 + h_num*R, y2), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))
#         else:
#             draw.ellipse((x1, y1 + h_num*R, x2, y2 + h_num*R), fill=(255, 255, 255, 255), outline=(0, 0, 0, 0))


# im.show()
# im.save('image/pillow_imagedraw.png', quality=100)
cv2.imwrite('image/cv2_imagedraw.png', blank_image)
