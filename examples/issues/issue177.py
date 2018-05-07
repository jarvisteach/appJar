import sys
sys.path.append("../../")

from appJar import gui

def move(btn):
    app.openSubWindow("New Sub")
    app.setLocation(app.getEntry("x"), app.getEntry("y"))
    app.stopSubWindow()

def moveT(btn):
    app.setLocation(app.getEntry("tx"), app.getEntry("ty"))

def box(btn):
    if btn == "numBox": app.numBox("Number", "Enter number")
    elif btn == "okBox": app.okBox("Number", "Enter number")
    elif btn == "textBox": app.textBox("Number", "Enter number")

app=gui()
app.addButton("New Sub", app.showSubWindow, colspan=2)
app.addNumericEntry("tx", column=0, row=1)
app.addNumericEntry("ty", column=1, row=1)
app.addButton("MOVE", moveT, colspan=2)
app.addButtons(["numBox", "okBox", "textBox"], box, colspan=2)

app.startSubWindow("New Sub")
app.addLabel("l1", "I'm a SubWindow", colspan=2)
app.addNumericEntry("x", column=0, row=1)
app.addNumericEntry("y", column=1, row=1)
app.addNamedButton("MOVE", "MOVET", move, colspan=2)
app.stopSubWindow()

app.go()
