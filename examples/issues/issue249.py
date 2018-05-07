import sys
sys.path.append("../../")
from appJar import gui

def DoExit(opt):
    if app.yesNoBox("Confirm exit","Exit sub window now?", parent="SUB1"):
        app.hideSubWindow("SUB1")

with gui("Example","400x200") as app:
    app.setLocation(100,100)

    with app.subWindow("SUB1", modal=True):
        app.addEntry("E1")
        app.addButton("Exit",DoExit)

    app.addNamedButton("SubWindow", "SUB1", app.showSubWindow)
    app.addButton("Quit", app.stop)
