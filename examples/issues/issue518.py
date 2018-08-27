import sys
sys.path.append("../../")

from numpy import sin, pi, arange
from appJar import gui 
import random

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    return {'t':x,'s':y}

def generate(btn):
    # *getXY() will unpack the two return values
    # and pass them as separate parameters
    app.plot("p1", **getXY())
    showLabels()

def showLabels():
    axes.legend(['The curve'])
    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
    app.refreshPlot("p1")

with gui() as app:
    axes = app.plot("p1", showNav=True, **getXY()) 
    showLabels()
    app.button("Generate", generate)
