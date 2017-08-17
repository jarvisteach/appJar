import sys
sys.path.append("../../")

def changed(widg):
    print(widg, "changed")

def change(widg):
    if widg == "SCALE":
        app.setScale("s1", 50, app.getCheckBox(widg))

from appJar import gui

app=gui()

app.addScale("s1")
app.setScaleChangeFunction("s1", changed)
app.addButton("SCALE", change)
app.addCheckBox("SCALE")

app.go()
