import sys
sys.path.append("../../")

from numpy import sin, pi, arange
from appJar import gui 
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg as addToolbar
import random

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10) * pi * x)
    return x,y 

with gui() as app:
    app.setLogLevel('ERROR')
    app.addPlot("p1", *getXY(), showNav=True)
