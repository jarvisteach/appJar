import sys
sys.path.append("../../")

from appJar import gui

def change(): print("changed")
def press(btn):
    if btn == "clear": app.clearListBox("list", callFunction=app.check("call"))
    else: app.updateListBox("list", ["d", "e", "f", "g"], callFunction=app.check("call"))

with gui() as app:
    app.label('hello world')
    app.listbox("list", ["a", "b", "c", "d"], change=change)
    app.check("call")
    app.buttons(["clear", "update"], press)
