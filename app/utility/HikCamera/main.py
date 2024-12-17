from HikCamera import *
import cv2
import sys, inspect

cam = Camera(ip='192.168.0.68')
cam.open()
cv2.imwrite("data2.jpeg", cam.get_frame())
cam.close()
