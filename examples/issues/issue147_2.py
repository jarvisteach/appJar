import sys
sys.path.append("../../")

from appJar import gui


def formatWindow(btn=None):
    app.startSubWindow("Angle Format", modal=True, blocking="True")
    app.startLabelFrame("The Bits")
    app.addLabel("Label1", "Please choose Angle Format for Excel Sheet")
    app.addRadioButton("AngType", "DMS Dashed")
    app.addRadioButton("AngType", "DMS stacked")
    app.addRadioButton("AngType", "Decimal Degrees")
    app.stopLabelFrame()
    app.addCheckBox("cb1")
    app.addNamedButton("OK", "Angle Format", app.destroySubWindow)
    app.addButtons(["a", "b", "c", "d"], None)
    app.stopSubWindow()
    app.showSubWindow("Angle Format")

app=gui()

app.addButton("PRESS", formatWindow)
app.go()
