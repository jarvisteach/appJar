#!/usr/bin/env python2

import sys
sys.path.append("../../")

import numpy as np
#import matplotlib.pyplot as plt
#from appJar import gui

from numpy import sin, pi, arange
from appJar import gui
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
import random

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    return x,y

with gui() as app:
    with app.frame('f1') as frame: pass
    app.addPlot("p1", *getXY())
    NavigationToolbar2TkAgg(app.getPlotWidget("p1"), frame)
    app.addMenuItem("appJar", "About", app.appJarAbout)
