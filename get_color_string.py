#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 9:54
# @Author  : ChenSiFan
# @Site    :
# @File    : get_color.py
# @Software: PyCharm

class GetColorString():
    def rgb2hsv(self,r, g, b):
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
        else:
            h = 0
        if mx == 0:
            s = 0
        else:
            s = m/mx
        v = mx
        return h, s, v

    def hsv2str(self,a):
        h=a[0]*0.5
        s=a[1]*255.0
        v=a[2]*255.0
        color = ""
        if (h>=0.0)     & (h<=180.0)    & (s>=0.0)  & (s<=255.0)& (v>=0.0)   & (v<=46.0):
            color = "黑"
        elif (h>=0)     & (h<=180.0)    & (s>=0)    & (s<=43)   & (v>=46)    & (v<=220):
            color = "灰"
        elif (h >= 0)   &( h <= 180)    & (s >= 0)  & (s <= 43) & (v >= 220) & (v <= 255):
            color = "白"
        elif ((h >= 0)  & (h <= 11))|((h >= 156)    & (h <= 180))& (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "红"
        elif (h >= 11)  & (h <= 26)     & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "橙"
        elif (h >= 26)  & (h <= 35)     & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "黄"
        elif (h >= 35)  & (h <= 78)     & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "绿"
        elif (h >= 78)  & (h <= 100)    & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "青"
        elif (h >= 100) & (h <= 125)    & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "蓝"
        elif (h >= 125) & (h <= 155)    & (s >= 43) & (s <= 255) & (v >= 46) & (v <= 255):
            color = "紫"
        else:
            print (h,s,v)
            print("不知道")
            color = "?"
        return color