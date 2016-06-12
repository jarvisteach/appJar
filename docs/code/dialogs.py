from appJar import gui

def press(btn):
    if btn == "info": app.infoBox("Title Here", "Message here...")
    if btn == "error": app.errorBox("Title Here", "Message here...")
    if btn == "warning": app.warningBox("Title Here", "Message here...")
    if btn == "yesno": app.yesNoBox("Title Here", "Message here...")
    if btn == "question": app.questionBox("Title Here", "Message here...")
    if btn == "ok": app.okBox("Title Here", "Message here...")
    if btn == "retry": app.retryBox("Title Here", "Message here...")
    if btn == "text": app.textBox("Title Here", "Message here...")
    if btn == "number": app.numberBox("Title Here", "Message here...")

app=gui()
app.addButtons(["info", "error", "warning", "yesno", "question"], press)
app.addButtons(["ok", "retry", "text", "number"], press)
app.go()
