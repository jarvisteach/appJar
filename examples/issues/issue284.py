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
    elif btn == "TEXT":
        val = app.textBox("a", "a")
    elif btn == "NUM":
        val = app.numBox("a", "a")
    print(type(val), val)

app = gui()
app.addButtons(["STRING", "INTEGER", "FLOAT", "TEXT", "NUM"], press)
app.go()
