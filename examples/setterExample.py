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

def ob(btn):
    app.setOptionBox("ob", app.getEntry("rb"))

def sb(btn):
    app.setSpinBox("sb", app.getEntry("rb"))

def scale(btn):
    print("sc")
    app.setScale(app.getEntry("rb"), 5)

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

app.startLabelFrame("OptionBox", 0, 3)
app.addOptionBox("ob", ["a", "b", "c", "d", "e", "aaaa"])
app.setOptionBoxFunction("ob", press)
app.stopLabelFrame()

app.startLabelFrame("Scale", 0, 4)
app.addScale("a")
app.addScale("b")
app.addScale("c")
app.addScale("d")
app.setScaleFunction("a", press)
app.setScaleFunction("b", press)
app.setScaleFunction("c", press)
app.setScaleFunction("d", press)
app.stopLabelFrame()

app.startLabelFrame("SpinBox", 0, 5)
app.addSpinBox("sb", ["a", "b", "c", "d", "e", "aaaa"])
app.setSpinBoxFunction("sb", press)
app.stopLabelFrame()

app.addEntry("rb", 1, 0)
app.addButtons(["RB", "CB", "LB", "OB", "SCALE", "SB"], [rb, cb, lb, ob, scale, sb], 1, 1, 6)

app.go()
