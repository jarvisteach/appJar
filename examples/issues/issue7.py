import sys
sys.path.append("../../")

def press(btn):
    global cb1, cb2
    print(cb1.cget("fg"), cb2.cget("fg"))
    app.setBg("green")
    print(cb1.cget("fg"), cb2.cget("fg"))
    app.setFg("yellow")
    print(cb1.cget("fg"), cb2.cget("fg"))
    cb1.config(fg="red")
    print(cb1.cget("fg"), cb2.cget("fg"))
from appJar import gui

app = gui("Colour Test")
app.setLogLevel("DEBUG")

app.setBg("Orange")
app.setFg("Blue")

app.addLabel("l1", "Main Colour Test")
cb1 = app.addCheckBox("This one")
cb2 = app.addNamedCheckBox("This one", "again")

app.addRadioButton("b1", "Radio")
app.addLabelRadioButton("b2", "Radio")

print(cb1.cget("fg"), cb2.cget("fg"))

app.addEntry("e1")
app.setEntryDefault("e1", "red")

app.addMessage("m2", "Mesage text wrapped up in a box...")
print(cb1.cget("fg"), cb2.cget("fg"))

app.startLabelFrame("Label Frame")
app.setFg("Pink")
app.addLabel("l2", "In the frame")
print(cb1.cget("fg"), cb2.cget("fg"))

app.startTabbedFrame("Tabs")
app.startTab("Tab 1")
app.addLabel("l3", "In tab 1")
app.setLabelFg("l3", "purple")
app.startLabelFrame("More Lables")
app.addLabel("l9", "In tab 1")
app.stopLabelFrame()
app.stopTab()
app.startTab("Tab 2")
app.addLabel("l5", "In tab 2")
app.stopTab()
app.startTab("Tab 3")
app.addLabel("l6", "In tab 3")
app.stopTab()
app.stopTabbedFrame()
print(cb1.cget("fg"), cb2.cget("fg"))

app.stopLabelFrame()

app.addButton("PRESS ME", press)
app.addMessage("m1", "Lots of writing")
print(cb1.cget("fg"), cb2.cget("fg"))

app.startToggleFrame("Options")
app.addCheckBox("ccb1")
app.addCheckBox("ccb2")
app.addCheckBox("ccb3")

app.setCheckBoxFg("ccb2", "green")
app.setCheckBox("ccb3")
app.stopToggleFrame()
print(cb1.cget("fg"), cb2.cget("fg"))


app.go()
