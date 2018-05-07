#!/usr/bin/env python3

from appJar import gui
from colour import Color
from PIL import ImageGrab
import numpy as np
import cv2

def press(name):
    image = ImageGrab.grab()
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # Convert RGB to BGR 
    im = open_cv_image[:, :, ::-1].copy() 
    cv2.namedWindow("Screenshot",cv2.WINDOW_NORMAL) 
    cv2.moveWindow("Screenshot", 0, 0) 
    r = cv2.selectROI("Screenshot", im, False)
    #cv2.waitKey()
    print("r is",r)


app = gui()
app.addButton("Screenshot",press)

app.go()
