import sys
sys.path.append("../../")

buttons = ["Status", "Settings", "About"]

from appJar import gui

def add(*args, **kwargs):
    app.addToolbar(buttons, delete)
    app.label("title", "old title", bg="red")

def delete(btn):
    app.label("title", "new title", bg="green")
    app.removeToolbar()

def addBits():
    app.removeAllWidgets()
    app.label("title")
    app.addButton("ADD", add)
    app.addButton("CLEAR", addBits)

with gui() as app:
    addBits()
    add()
