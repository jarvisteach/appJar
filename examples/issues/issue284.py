import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn == "STRING":
        val = app.stringBox("a", "a")
    elif btn == "INTEGER":
        val = app.integerBox("a", "a")
    elif btn == "FLOAT":
        val = app.floatBox("a", "a")
    print(type(val), val)

app = gui()
app.addButtons(["STRING", "INTEGER", "FLOAT"], press)
app.go()
