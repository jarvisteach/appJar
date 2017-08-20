import sys
sys.path.append("../../")

def press(btn):
    app.playSound("song1.wav")
    if btn == "PRESS":
        print(app.translate("msg1"))
        app.okBox("OK", "EMPTY")
    elif btn == "PRESS2":
        print(app.translate("msg2", "the default"))
        app.okBox("OTHER", "STILL EMPTY")

from appJar import gui

app=gui()
app.addLabel("l1", "DEFAULT")
app.addLabel("l2", "DEFAULT")
app.addLabel("l3", "DEFAULT")
app.addButtons(["PRESS", "PRESS2"], press)
app.go("ENGLISH")
