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
    if val == "info": app.infoBox("a", "a")
    elif val == "error": app.errorBox("a", "a")
    elif val == "warn": app.warningBox("a", "a")
    elif val == "yesno": app.yesNoBox("a", "a")
    elif val == "question": app.questionBox("a", "a")
    elif val == "ok": app.okBox("a", "a")
    elif val == "retry": app.retryBox("a", "a")
    elif val == "text": app.textBox("a", "a")
    elif val == "number": app.numberBox("a", "a")
    print("here")

app = gui()
app.addOptionBox("choice", ["info", "error", "warn", "yesno", "question", "ok", "text", "number"])
app.addButton("PRESS", popUp)
app.registerEvent(closePop)
app.setPollTime(1000)
app.go()

