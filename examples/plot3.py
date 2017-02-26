import sys
sys.path.append("../")
from appJar import gui

x = [1,2,3,4,5]
y = [2,4,6,8,10]

app = gui()
axes = app.addPlot("p1", x, y)
axes.legend(['key data'])
app.go()
