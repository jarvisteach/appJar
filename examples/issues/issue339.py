import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "ADD": app.addToolbarButton("E", press)
    else: app.removeToolbarButton(btn, hide=False)

def again(btn=None):
    app.addToolbar(["A", "B", "C", "D"], press)

def remove(btn):
    app.removeToolbar()

with gui() as app:
    again()
    app.label("a", "Press a button")
    app.addButtons(["AGAIN", "ADD", "ALL"], [again, press, remove])
#    app.setToolbarPinned()
