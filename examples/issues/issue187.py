import sys
sys.path.append("../../")

from appJar import gui
app=gui()
app.addCheckBox("b1")
app.addRadioButton("b1", "b1")
app.addButton("BUTTON", None)

app.setFg("pink")
app.setBg("blue")
app.go()
