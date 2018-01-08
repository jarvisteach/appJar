import sys
sys.path.append("../../")

buttons = ["Status", "Settings", "About"]

from appJar import gui

def add(btn=None):
    app.addToolbar(buttons, delete)
    print(app.label("title"))
    app.label("title", "old title", bg="red")

def delete(btn=None):
    print(app.label("title"))
    app.label("title", "new title", bg="green")
    app.removeToolbar()

with gui() as app:
    app.label("title")
    app.addButton("ADD", add)
    add()
