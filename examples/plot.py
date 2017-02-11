#import matplotlib
#matplotlib.use('TkAgg')
from numpy import arange, sin, pi
import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    t = arange(0.2, 12.0, 0.01)
    s = sin(4*pi*t)
    app.updatePlot("p1", t, s)

t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)

app = gui()
app.startLabelFrame("MatPlotLib")
app.addLabel("l1", "Welcome to MatPlotLib")
axes = app.addPlot("p1", t, s)
axes.legend(['some stuff'])
app.addButtons(["Quit", "Open", "Close"], press)
app.stopLabelFrame()
app.go()
