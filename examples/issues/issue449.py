import sys
sys.path.append("../../")

from appJar import gui

def change(): print("changed")
def press(btn):
    if btn == "clear": app.clearListBox("list", callFunction=app.check("call"))
    elif btn == "select":
        app.selectListItemAtPos("list", -5, callFunction=app.check("call"))
        app.selectListItemAtPos("list", 0, callFunction=app.check("call"))
        app.selectListItemAtPos("list", 40, callFunction=app.check("call"))
        app.selectListItemAtPos("list", 4, callFunction=app.check("call"))
        app.selectListItemAtPos("list", 3, callFunction=app.check("call"))
        app.selectListItem("list", "a", callFunction=app.check("call"))
        app.selectListItem("list", ["a", "b"], callFunction=app.check("call"))
        app.selectListItem("list", ["a", "f"], callFunction=app.check("call"))
    else: app.updateListBox("list", ["d", "e", "f", "g"], callFunction=app.check("call"))

with gui() as app:
    app.label('hello world')
    app.listbox("list", ["a", "b", "c", "d"], change=change)
    app.check("call")
    app.buttons(["select", "clear", "update"], press)
