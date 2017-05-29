import sys
sys.path.append("../../")

from appJar import gui

app = gui()
app.addLabel("l0", "basic label")
app.setLabelBg("l0", "yellow")
app.setLabelFg("l0", "blue")

app.addSelectableLabel("l1", "Select all the text...")
app.setLabelBg("l1", "red")
app.setLabelFg("l1", "yellow")

app.addEntry("e1")
app.setEntryBg("e1", "green")

lab = app.getLabelWidget("l1")
print(lab.cget("fg"))

app.setFont(20)

print(app.getLabel("l1"))

def press(btn): app.clearLabel("l1")
app.addButton("PRESS", press)

app.go()
