import sys
sys.path.append("../")

from appJar import gui

def press(btn):
    print("function called:", btn)

def rb(btn):
    app.setRadioButton("song", app.getEntry("rb"))

def cb(btn):
    app.setCheckBox(app.getEntry("rb"))

def lb(btn):
    app.selectListItem("lb", app.getEntry("rb"))

app = gui()

app.startLabelFrame("RadioButtons", 0, 0)
app.addRadioButton("song", "a")
app.addRadioButton("song", "b")
app.addRadioButton("song", "c")
app.addRadioButton("song", "d")
app.setRadioButtonFunction("song", press)
app.stopLabelFrame()


app.startLabelFrame("CheckBox", 0, 1)
app.addCheckBox("a")
app.setCheckBoxFunction("a", press)
app.addCheckBox("b")
app.setCheckBoxFunction("b", press)
app.addCheckBox("c")
app.setCheckBoxFunction("c", press)
app.addCheckBox("d")
app.setCheckBoxFunction("d", press)
app.stopLabelFrame()

app.startLabelFrame("ListBox", 0, 2)
app.addListBox("lb", ["a", "b", "c", "d", "e"])
app.setListBoxFunction("lb", press)
app.stopLabelFrame()

app.addEntry("rb", 1, 0)
app.addButtons(["RB", "CB", "LB"], [rb, cb, lb], 1, 1, 2)

app.go()
