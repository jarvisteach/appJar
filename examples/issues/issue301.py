import sys
sys.path.append("../../")

def press(btn): print(btn)

from appJar import gui

with gui() as app:
    app.label("a", "Hello world")
    app.label("b", "Hello world")
    app.grip(0,1)
    app.button("a", press)
    app.button("b", press)
    app.button("c", press)

