import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    if btn == "btn":
        print(app.textBox("text", "text"))
    elif btn == "btn2":
        print(app.numberBox("num", "num"))

app=gui()
app.addLabel("l1", "Label")
app.addButtons(["btn", "btn2"], press)
app.go()
