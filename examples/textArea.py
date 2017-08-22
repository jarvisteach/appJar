import sys
sys.path.append("../")
from appJar import gui

def press(btn=None):
    if btn == "CLEAR":
        app.clearTextArea("t1", callFunction=app.getCheckBox("CALL"))
    elif btn == "SET":
        app.setTextArea("t1", app.getEntry("text"), callFunction=app.getCheckBox("CALL"), end=app.getCheckBox("END"))
    else:
        print("changed:", btn)

def log(btn):
    if btn == "LOG":
        app.logTextArea("t1")
    elif btn == "CHECK":
        print(app.textAreaChanged("t1"))


app=gui()

app.addScrolledTextArea("t1")
app.setTextAreaChangeFunction("t1", press)
app.addButtons(["CLEAR", "SET"], press)
app.addButtons(["LOG", "CHECK"], log)
app.addCheckBox("CALL")
app.addCheckBox("END")
app.addEntry("text")

app.go()
