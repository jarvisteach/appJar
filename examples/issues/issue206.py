import sys
sys.path.append("../../")

def changed(widg):
    print(widg, "changed")

def change(widg):
    if widg == "SCALE":
        app.setScale("a", 50, app.getCheckBox(widg))
    elif widg == "OB":
        app.changeOptionBox("a", ["- Fruits -", "Apple", "Orange",
                "Pear", "kiwi", "- Pets -", "Dogs", "Cats",
                "Fish", "Hamsters"], callFunction=app.getCheckBox(widg))
    elif widg == "RB":
        app.setRadioButton("a", "b", callFunction=app.getCheckBox(widg))
    elif widg == "TB":
        app.setCheckBox("a", True, callFunction=app.getCheckBox(widg))
    elif widg == "ENT":
        app.clearEntry("a", callFunction=app.getCheckBox(widg))
        app.setEntry("a", "Changed it", callFunction=app.getCheckBox(widg))

from appJar import gui

app=gui()

app.addCheckBox("SCALE", row=0, column=0)
app.addCheckBox("OB", row=0, column=1)
app.addCheckBox("RB", row=0, column=2)
app.addCheckBox("TB", row=0, column=3)
app.addCheckBox("ENT", row=0, column=4)

app.addButtons(["SCALE", "OB", "RB", "TB", "ENT"], change, colspan=5)

app.startLabelFrame("Widgets", colspan=5)
app.setSticky("EW")
app.addScale("a")
app.addOptionBox("a", ["- Fruits -", "Apple", "Orange",
                "Pear", "kiwi", "- Pets -", "Dogs", "Cats",
                "Fish", "Hamsters"])

app.addRadioButton("a", "a")
app.addRadioButton("a", "b")
app.addCheckBox("a")
app.addEntry("a")
app.stopLabelFrame()

app.setScaleChangeFunction("a", changed)
app.setOptionBoxChangeFunction("a", changed)
app.setRadioButtonChangeFunction("a", changed)
app.setCheckBoxChangeFunction("a", changed)
app.setEntryChangeFunction("a", changed)

app.go()
