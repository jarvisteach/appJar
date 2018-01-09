import sys
sys.path.append("../../")

buttons = ["Status", "Settings", "About"]

from appJar import gui

def add(*args, **kwargs):
    print(args)
    app.addToolbar(buttons, delete)
    print(app.label("title"))
    app.label("title", "old title", bg="red")

def delete(btn):
    print(app.label("title"))
    app.label("title", "new title", bg="green")
    app.removeToolbar()

def addBits():
    app.removeAllWidgets()
    print("adding empty label")
    app.label("title")
    app.addButton("ADD", add)
    app.addButton("CLEAR", addBits)

with gui() as app:
    addBits()
    add()
