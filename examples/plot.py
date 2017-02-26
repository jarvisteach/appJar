#import matplotlib
#matplotlib.use('TkAgg')
from numpy import arange, sin, pi
import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    t = arange(0.2, 20.0, 0.1)
    s = sin(int(app.getEntry("space"))*pi*t)
    app.updatePlot("p1", t, s)

t = arange(0.0, 3.0, 0.01)
s = sin(2*pi*t)

app = gui()
app.startLabelFrame("MatPlotLib Example")
app.setSticky("ew")
axes = app.addPlot("p1", t, s, colspan=2)
axes.legend(['some stuff'])
app.addEntry("space", row=1, column=0)
app.addButton("Update", press, row=1, column=1)
app.stopLabelFrame()
app.go()
