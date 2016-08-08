from appJar import gui

def press(btn):
    if btn == "CLEAR":
        app.clearStatus()
        return
    if btn != "None": btn=int(btn)
    else: btn=None
    app.setStatus(app.getEntry("e1"), btn)
    app.setStatusWidth(int(app.getEntry("e1")), btn)

app=gui()

app.addStatus(fields=5)
app.setStatusBg("blue")
app.setStatusFg("white", 3)
app.addEntry("e1")
app.addButtons(["None", "0", "1", "2", "3", "4", "CLEAR"], press)
app.go()
