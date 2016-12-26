import sys

sys.path.append("../../../")
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

app.addCheckBox("b1")
app.addCheckBox("b2")
app.addCheckBox("b3")

app.addLink("l1", None)
app.addWebLink("l2", "http://www.appJar.info")

app.addMeter("m1")

app.go(language="ENGLISH")
