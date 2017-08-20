import sys
sys.path.append("../../")

def press(btn):
    if btn == "PRESS":
        app.playSound("notify.wav")
        print(app.translate("msg1"))
        app.okBox("OK", "EMPTY")
    elif btn == "PRESS2":
        app.playSound("ringout.wav")
        print(app.translate("msg2", "the default"))
        app.okBox("OTHER", "STILL EMPTY")

from appJar import gui

app=gui()
app.setLogLevel("DEBUG")
app.setSoundLocation("C:\Windows\Media")
app.addLabel("l1", "DEFAULT")
app.addLabel("l2", "DEFAULT")
app.addLabel("l3", "DEFAULT")
app.addButtons(["PRESS", "PRESS2"], press)
app.addButtons(["ENGLISH", "FRENCH"], app.changeLanguage)
app.go("ENGLISH")
