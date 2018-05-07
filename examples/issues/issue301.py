import sys
sys.path.append("../../")

def press(btn): print(btn)

from appJar import gui

with gui() as app:
    app.label("a", "Hello world")
    app.label("b", "Hello world")
    app.grip(pos=(0,1))
    app.button("a", press, col=1)
    app.button("b", press, col=1)
    app.button("c", press, col=1)

