import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    print(app.getSpinBox("Options"))
    print(app.getSpinBox("Numbers"))

app=gui()
app.setFont(20)
app.addSpinBoxRange("Numbers", 1, 12)
app.go()
