import sys
sys.path.append("../../")

from appJar import gui

def change():
    print("changed", app.spin("a"))

def update():
    app.setSpinBox("a", "c", app.check("c"))

with gui() as app:
    app.label('hello world')
    app.spin("a", ["a", "b", "c", "d", "e"], change=change)
    app.check("c")
    app.button("PRESS", update)
