import sys
sys.path.append("../")

from appJar import gui

def get(btn):
    print(app.getFocus() == btn)

def press(btn):
    if btn == "E1": app.setEntryFocus("e1")
    if btn == "L1": app.setLabelFocus("l1")

app = gui()
e1 = app.addEntry("e1")
e1 = app.addLabel("l1")

app.addButtons(["E1", "L1"], press)
app.addButtons(["l1", "e1"], get)

app.go()
