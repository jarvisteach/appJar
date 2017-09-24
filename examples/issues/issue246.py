import sys
sys.path.append("../../")

from appJar import gui

app = gui()
app.startLabelFrame("lf1", hideTitle=True)
app.addLabel("l1", "In the frame")
app.stopLabelFrame()

with app.labelFrame("lf2", hideTitle=True):
    app.addLabel("l2", "In the frame")

app.go()
