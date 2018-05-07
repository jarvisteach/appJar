import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(app.questionBox("a", "a"))

app = gui()
app.addButton("PRESS", press)
app.go()
