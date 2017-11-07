import sys
sys.path.append("../../")

def press(btn):
    if btn == "SUB":
        app.showSubWindow("Sub")
        app.hide()
    if btn == "POPUP":
        app.infoBox("INFO", "INFO")

from appJar import gui

with gui("Main Window") as app:
    app.label("title", "Main Window")
    app.button("SUB", press)

    with app.subWindow("Sub"):
        app.label("sub", "SubWindow")
        app.button("POPUP", press)

    app.hide()
    app.showSubWindow("Sub")
