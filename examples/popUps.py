import sys
sys.path.append("../")
from appJar import gui

def closePop():
    POP_UP = app.getPopUp()
    print("closing:", app.getPopUp())
    if POP_UP is not None: POP_UP.cancel()

def popUp(btn):
    val = app.getOptionBox("choice")
    print(val)
    if val == "info": app.infoBox("a", "a", parent="sub1")
    elif val == "error": app.errorBox("a", "a", parent="sub1")
    elif val == "warn": app.warningBox("a", "a", parent="sub1")
    elif val == "yesno": app.yesNoBox("a", "a", parent="sub1")
    elif val == "question": app.questionBox("a", "a", parent="sub1")
    elif val == "ok": app.okBox("a", "a", parent="sub1")
    elif val == "retry": app.retryBox("a", "a", parent="sub1")
    elif val == "text": app.textBox("a", "a", parent="sub1")
    elif val == "number": app.numberBox("a", "a", parent="sub1")
    elif val == "open": app.openBox("open", parent="sub1")
    elif val == "save": app.saveBox("save", parent="sub1")
    elif val == "directory": app.directoryBox("directory", parent="sub1")
    elif val == "colour": app.colourBox(app.getEntry("colour"), parent="sub1")
    print("here")

with gui(startWindow="sub1", language="FRENCH") as app:
    with app.subWindow("sub1"):
        app.addOptionBox("choice", ["info", "error", "warn", "yesno", "question", "ok", "text", "number", "open", "save", "directory", "colour"])
        app.addButton("PRESS", popUp)
        app.addEntry("colour")
        app.setStopFunction(app.stop)

    app.registerEvent(closePop)
    app.setPollTime(1000)
