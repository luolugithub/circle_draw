# -*- coding: utf-8 -*-
# @Time    : 2020/7/30 上午9:56
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : percentage_color.py
# @Software: PyCharm
import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator

import extcolors
import PIL


img = PIL.Image.open("image/c500_median_contact.png")
print(type(img))
colors, pixel_count = extcolors.extract_from_image(img)
print(colors)
print(pixel_count)