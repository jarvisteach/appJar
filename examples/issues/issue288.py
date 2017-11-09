import sys
sys.path.append("../../")

def press(btn):
    if btn == "SUB":
        app.showSubWindow("Sub")
        app.hide()
    if btn in ["POPUP2",  "POPUP"]:
        app.infoBox("INFO", "INFO")
    if btn == "MAIN":
        app.show()
        app.hideSubWindow("Sub")

def closer(btn=None):
    print("aaa")

from appJar import gui

with gui("Main Window", startWindow="Sub") as app:
#with gui("Main Window") as app:
    app.label("title", "Main Window")
    app.button("POPUP", press)

    with app.subWindow("Sub"):
        app.label("sub", "SubWindow")
        app.button("POPUP2", press)
        app.button("MAIN", press)
        app.setStopFunction(closer)

#    app.hide()
#    app.showSubWindow("Sub")
