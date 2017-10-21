import sys
sys.path.append("../../")
from appJar import gui

def change(btn=None):
    app.removeAllWidgets()
    app.addLabel("nl1", "More text")
    app.addScrolledTextArea("t12")
    app.addButton("Press", back)

def back(btn=None):
    app.removeAllWidgets()
    app.setGeom("400x400")
    app.startLabelFrame("lf1")
    app.addLabel("l1", "Name:", 0, 0)
    app.addLabel("l2", "Name:", 1, 0)
    app.addLabel("l3", "Name:", 2, 0)
    app.addEntry("e1",  0, 1)
    app.addEntry("e2",  1, 1)
    app.addEntry("e3",  2, 1)
    app.addLabel("l4", "some more text", 3, 0, colspan=2)
    app.stopLabelFrame()

    app.addButtons(["Scan", "connect"], change)

app=gui()
back()
app.go()

