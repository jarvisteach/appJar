import sys

sys.path.append("../../")
from appJar import gui

def press(btn):
    app.changeLanguage(btn)
app=gui()
app.showSplash()

app.addLabel("l1", "default text")
app.addButtons(["English", "Korean", "French"], press)
app.addLabel("l2", "default text")
app.addLabel("l3", "default text")
app.addLabelEntry("Genome")
app.addLabelScale("s1")
app.addMessage("m1", "Default message text")

app.addListBox("fruits", ["apples", "oranges", "tomatoes"])
app.addOptionBox("fruits", ["apples", "oranges", "tomatoes"])
app.addSpinBox("fruits", ["apples", "oranges", "tomatoes"])

app.addCheckBox("b1")
app.addCheckBox("b2")
app.addCheckBox("b3")

app.startLabelFrame("Names")
app.addRadioButton("name", "b1")
app.addRadioButton("name", "b2")
app.addRadioButton("name", "b3")
app.addRadioButton("name", "b4")
app.stopLabelFrame()

app.addRadioButton("age", "b1")
app.addRadioButton("age", "b2")
app.addRadioButton("age", "b3")

app.addLink("l1", None)
app.addWebLink("l2", "http://www.appJar.info")

app.addMeter("m1")
app.addEntry("e1")
app.addEntry("e2")
app.setEntryDefault("e1", "<DEFAULT>")

app.go(language="ENGLISH")
