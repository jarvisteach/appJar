import sys
sys.path.append("../../")

def press(btn):
    val = app.getCheckBox("Tick me")
    app.setCheckBox("Tick me", not val)

from appJar import gui
app = gui("ttk demo")
app.label("aaa", "Main Title")
with app.labelFrame("LabelFrame"):
#    with app.notebook("nb"):
#        with app.note("note1"):
    app.addToolbar(["OPEN", "CLOSE"], press, findIcon=True)
    app.addLabel("l1", "Simple Label")
    app.addCheckBox("Tick me")
    app.addRadioButton("tb", "Tick me")
    app.addTextArea("t1")
    app.addButton("Press Me", None)
    app.addSpinBoxRange("spinner", 1, 10)
    app.addScale("Scale")
    app.addEntry("Entry")
    app.setEntryTooltip("Entry", "help me")
    app.addButtons(["a", "b", "c"], None)
    app.addLabelEntry("fill me")
    app.addLabels(["a", "b", "c"])
    app.addMessage("mess", "some message text")
    app.button("TICK", press)
#        with app.note("note2"):
 #           pass
#app.setBg("green")

app.go()
