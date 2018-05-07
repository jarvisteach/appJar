import sys
sys.path.append("../../")
from appJar import gui

toolbar_list = ["Status", "settings", "about"]

def press(btn):
    if btn == "ADD":
        app.addToolbarButton("E", press)
    else:
        app.removeToolbarButton(btn, hide=False)
        app.removeStatusbarField(2)

def again(btn=None):
    app.addStatusbar(fields=5)
    app.setStatusbar("a", 0)
    app.setStatusbar("b", 1)
    app.setStatusbar("c", 2)
    app.setStatusbar("d", 3)
    app.addToolbar(toolbar_list, press)

def remove(btn):
    app.removeToolbar()
    app.removeStatusbar()

with gui() as app:
    again()
    app.label("a", "Press a button")
    app.addButtons(["ADD ALL", "ADD", "REMOVE ALL"], [again, press, remove])
#    app.setToolbarPinned()
