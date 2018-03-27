import sys
sys.path.append("../../")

def press(btn):
    if btn == "a": app.size="700x200"
    elif btn == "b": app.setSize("200x700")
    elif btn == "c": app.size=(400,400)
    elif btn == "d": app.setSize(600,600)

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.buttons(['a', 'b', 'c', 'd'], press)
