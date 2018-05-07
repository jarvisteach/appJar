import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    with app.frame("ONE", 0,0):
        app.label("In frame one")
    with app.frame("TWO", 0,0):
        app.label("In frame two")
    app.buttons(["ONE", "TWO"], app.raiseFrame)
