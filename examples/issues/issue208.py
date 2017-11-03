import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "SUB":
        app.showSubWindow("Sub Window", follow="topLevel")
    if btn == "SUBBER":
        app.showSubWindow("subber", follow="Sub Window")
    if btn == "LOCATION":
        app.setLocation(90,90)
    if btn == "FULL":
        app.setFullscreen()

with gui("Main Window") as app:
#    app.setLocation(300,300)#, ignoreSettings=True)
 #   app.setSize(150,150)
    app.addGrip()

    app.addLabel("title", "Main Window")
    app.addButton("SUB", press)
    app.addButton("EXIT", press)
    app.addButton("LOCATION", press)
    app.addButton("FULL", press)

    with app.subWindow("Sub Window"):
        app.addLabel("sub_title", "Sub Window")
        app.setFullscreen()
        app.addButton("SUBBER", press)
        app.setStopFunction(app.stop)

    with app.subWindow("subber"):
        app.addLabel("subber", "In subber")
        app.setStopFunction(app.stop)

    with app.subWindow("subber2"):
        app.addLabel("subber2", "In subber")
        app.setStopFunction(app.stop)
