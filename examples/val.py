import sys
sys.path.append("../")

def press(btn):
    if btn == "YES": app.setEntryValid("a")
    elif btn == "NO": app.setEntryInvalid("a")
    elif btn == "WAIT": app.setEntryWaitingValidation("a")

from appJar import gui

app=gui()
app.addEntry("aa")
app.addValidationEntry("a")
app.addEntry("bb")
app.setEntryMaxLength("a", 5)
app.addButtons(["YES", "NO", "WAIT"], press)
app.go()
