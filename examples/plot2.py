import sys
sys.path.append("../")
from numpy import sin, pi, arange
from appJar import gui

x = arange(0.0, 3.0, 0.01)
y = sin(2*pi*x)

app = gui()
axes = app.addPlot("p1", x, y)
axes.legend(['key data'])
app.go()
