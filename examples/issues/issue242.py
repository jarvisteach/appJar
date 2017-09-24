import sys
sys.path.append("../../")
from numpy import sin, pi, arange
from appJar import gui
import random

def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1,10)*pi*x)
    return x,y

def generate(btn):
    app.updatePlot("p1", *getXY(), keepLabels=True)
#    showLabels()

def showLabels():
    axes = app.getWidget(app.PLOT, "p1").axes
    axes.legend(['The curve'])

    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
    axes.set_title("Demo Data")
    app.refreshPlot("p1")

app = gui()
app.addPlot("p1", *getXY())
showLabels()
app.addButton("Generate", generate)
app.go()
