import sys
sys.path.append("../../")

def press(b):
    if b == "U":
        t.fd(100)
    if b == "U":
        app.getTurtleScreen("r1")

from appJar import gui
app=gui()
t = app.addTurtle("t1")
r = app.addTurtle("r1")
app.addButtons(["L", "R", "U", "D"], press)
app.go()
