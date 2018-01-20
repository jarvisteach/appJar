import sys
sys.path.append("../../")

from appJar import gui
app = gui()

def press(name):
    if name == "Enter":
        name = app.getEntry("e1")
        app.setLabel("lb3", "Welcome " + name)
        app.hideSubWindow("sb1")
        app.showSubWindow("sb2")
    elif name == "Exit":
        app.stop()

app.startSubWindow("sb1")
app.addLabel("lb1", "This is a label inside sb1.")
app.addLabel("lb4", "What is your name?", 1,0)
app.addEntry("e1", 1,1)
app.addButton("Enter", press)
app.stopSubWindow()

app.startSubWindow("sb2")
app.addLabel("lb2", "This is a label inside sb1.")
app.addLabel("lb3", "name unknown")
app.addButton("Exit", press)
app.stopSubWindow()

app.go(startWindow="sb1")
