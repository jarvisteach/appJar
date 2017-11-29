import sys
sys.path.append("../../")

def press(btn):
    if btn == "CLEAR":
        app.removeAllWidgets()
        app.addButtons(["CLEAR", "RESET"], press, 2, colspan=2)
    else:
        addWidgets()

from appJar import gui


def addWidgets():
    app.setBg("blue")
    app.setStretch("both")

    app.setSticky("nw")
    app.addLabel("l1", "One", 0, 0)
    app.setLabelBg("l1", "yellow")

    app.setSticky("ne")
    app.addLabel("l2", "Two", 0, 1)
    app.setLabelBg("l2", "green")

    app.setSticky("sw")
    app.addLabel("l3", "Three", 1, 0)
    app.setLabelBg("l3", "pink")

    app.setSticky("se")
    app.addLabel("l4", "Four", 1, 1)
    app.setLabelBg("l4", "Orange")


app=gui("400x400")
addWidgets()
app.addButtons(["CLEAR", "RESET"], press, 2, colspan=2)
app.go()
