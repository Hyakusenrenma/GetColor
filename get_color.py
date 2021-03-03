#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 9:54
# @Author  : ChenSiFan
# @Site    : 
# @File    : get_color.py
# @Software: PyCharm
from PIL import ImageGrab
import time
import pyautogui as pag
from tkinter import *
from get_color_string import GetColorString
from grab_point import Grab_point

def init_app():
    global root
    global stringVar
    global get_color_string
    root_geometry = "80x30+10+10"
    get_color_string = GetColorString()
    root =  Tk()
    stringVar = StringVar()
    root.wm_attributes('-topmost',1)
    root.overrideredirect(True)
    root.attributes("-alpha", 0.7)
    root.geometry(root_geometry)
    label = Label(root,textvariable=stringVar,font=("微软雅黑", 20),relief=RIDGE)
    label.configure(width = 80,height = 30,bg = "white",highlightthickness = 0)
    label.pack()

init_app()

def set_root_geometry(tmp_root,string):
    tmp_root.geometry(string)




while(1):
    n_x, n_y = pag.position()
    now_grab_point =  Grab_point(n_x,n_y)
    image = ImageGrab.grab((now_grab_point.point_x_l,now_grab_point.point_y_l,now_grab_point.point_x,now_grab_point.point_y))
    set_root_geometry(root,"80x30+"+str(n_x+10)+"+"+str(n_y+10))
    pixel = image.getpixel((0, 0))
    stringVar.set(get_color_string.hsv2str(get_color_string.rgb2hsv(pixel[0], pixel[1], pixel[2])))
    root.update()
    time.sleep(0.1)
