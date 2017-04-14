import sys
sys.path.append("../../")
from appJar import gui

def sw1(btn):
    c = "sw1"
    doIt(c, btn.lower())

def action(btn):
    c = app.getOptionBox("container")
    doIt(c, btn.lower())

def doIt(c, btn):
    if btn == "destroy":
        print("Destroying container", c)
        app.destroySubWindow(c)
    elif btn == "hide":
        print("Hiding container", c)
        app.hideSubWindow(c)
    elif btn == "show":
        print("Showing container", c)
        app.showSubWindow(c)

app=gui("Testing Destruction")

app.addLabel("l1", "Testing Destroying Containers")
app.addOptionBox("container", ["-- choose a container --", "sw1"])
app.addButtons(["destroy", "hide", "show"], action)

app.startSubWindow("sw1", modal=True, blocking=True)
app.addLabel("sl", "SubWindow One")
app.addButtons(["Destroy", "Hide"], sw1)
app.startLabelFrame("lf1")
app.addLabel("lf1_lab", "Label Frame 1")
app.startLabelFrame("lf2")
app.addLabel("lf2_lab", "Label Frame 1")
app.startLabelFrame("lf3")
app.addLabelEntry("eee1")
app.addLabel("lf3_lab", "Label Frame 1")
app.stopLabelFrame()
app.stopLabelFrame()
app.stopLabelFrame()
app.stopSubWindow()

app.go()
