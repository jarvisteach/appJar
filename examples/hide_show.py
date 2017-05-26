import sys
sys.path.append("../")
from appJar import gui


def press(btn):
    val = app.getEntry("e1")
    if btn == "hide":
        app.hideLabel(val)
    elif btn == "show":
        app.showLabel(val)
    elif btn == "remove":
        app.removeLabel(val)

app=gui()
for x in range(3):
    for y in range(5):
        key = "LAB_" + str(x) + str(y) 
        app.addLabel(key, key, x, y)


app.addButtons(["hide", "show", "remove"], press, colspan=5)
app.addEntry("e1", colspan=5)
app.setEntry("e1", "LAB_11")
app.go()
