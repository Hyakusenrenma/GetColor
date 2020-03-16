#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 9:54
# @Author  : ChenSiFan
# @Site    : 
# @File    : getColor.py
# @Software: PyCharm
from PIL import ImageGrab
import time
import pyautogui as pag


def rgb2hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    m = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        if g >= b:
            h = ((g-b)/m)*60
        else:
            h = ((g-b)/m)*60 + 360
    elif mx == g:
        h = ((b-r)/m)*60 + 120
    elif mx == b:
        h = ((r-g)/m)*60 + 240
    if mx == 0:
        s = 0
    else:
        s = m/mx
    v = mx
    return h, s, v

def hsv2str(a):
    h=a[0]*0.5
    s=a[1]*255.0
    v=a[2]*255.0
    if (h>=0.0) & (h<=180.0) & (s>=0.0) & (s<=255.0) & (v>=0.0) & (v<=46.0):
        print("黑")
    elif (h>=0) & (h<=180.0) & (s>=0) & (s<=43) & (v>=46) & (v<=220):
        print("灰")
    elif (h >= 0) &( h <= 180) & (s >= 0) & (s <= 30) & (v >= 221) & (v <= 255):
        print("白")
    elif ((h >= 0) & (h <= 10))|((h >= 156) & (h <= 180)) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("红")
    elif (h >= 11) & (h <= 25) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("橙")
    elif (h >= 26) & (h <= 34) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("黄")
    elif (h >= 35) & (h <= 77) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("绿")
    elif (h >= 78) & (h <= 99) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("青")
    elif (h >= 100) & (h <= 124) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("蓝")
    elif (h >= 125) & (h <= 155) & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
        print("紫")
    else:
        print("不知道")
while(1):
    image = ImageGrab.grab()
    n_x, n_y = pag.position()
    a = image.getpixel((n_x, n_y))
    hsv2str(rgb2hsv(a[0], a[1], a[2]))
    time.sleep(1)

