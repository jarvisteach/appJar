import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "Enable":
        app.enableLabelTooltip("l1")
    elif btn == "Disable":
        app.disableLabelTooltip("l1")
    elif btn == "Change":
        app.setLabelTooltip("l1", app.getEntry("e1"))

app=gui()

app.addLabel("l1", "Hover here to see a tooltip...")
app.setLabelTooltip("l1", "Lots of tooltip text")
app.addButtons(["Enable", "Disable", "Change"], press)
app.addEntry("e1")
app.go()
