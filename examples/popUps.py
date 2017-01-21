from appJar import gui

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

app = gui()
app.addOptionBox("choice", ["info", "error", "warn", "yesno", "question", "ok", "text", "number"])
app.addButton("PRESS", popUp)
app.go()

