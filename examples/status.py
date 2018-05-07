import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    if btn == "CLEAR":
        app.clearStatusbar()
        return
    if btn != "None": btn=int(btn)
    else: btn=None
    
    app.setStatusbar(app.getEntry("e1"), btn)
    app.setStatusbarWidth(int(app.getEntry("e1")), btn)

app=gui()

app.addStatusbar(fields=5)
app.setStatusbarHeader("this one")
app.setStatusbarBg("blue")
app.setStatusbarFg("white", 3)
app.addEntry("e1")
app.addButtons(["None", "0", "1", "2", "3", "4", "CLEAR"], press)
app.go()
