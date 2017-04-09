import sys
sys.path.append("../../")

def press(btn):
    print("in but")
    if btn == "YES":
        app.setEntryValid("a")
        app.setEntryValid("Check out my label")
    elif btn == "NO":
        app.setEntryInvalid("a")
        app.setEntryInvalid("Check out my label")
    elif btn == "WAIT":
        app.setEntryWaitingValidation("a")
        app.setEntryWaitingValidation("Check out my label")

    if btn == "YES": app.setEntryValid("n")
    elif btn == "NO": app.setEntryInvalid("n")
    elif btn == "WAIT": app.setEntryWaitingValidation("n")

    if btn == "red": app.setBg("red")
    if btn == "green": app.setBg("green")
    if btn == "white": app.setBg("white")

    if btn == "up": app.increaseFont()
    if btn == "mid": app.setFont(15)
    if btn == "down": app.decreaseFont()
    print("out but")

from appJar import gui

app=gui()
app.setBg("yellow")
app.addEntry("n")
app.addLabelEntry("Labelled")
app.addLabelEntry("Stuff")
app.addValidationEntry("a")
app.addLabelValidationEntry("Check out my label")
app.setEntryDefault("a", "--valid--")
app.addValidationEntry("b")
app.setEntryDefault("b", "--invalid--")
app.addValidationEntry("c")
app.setEntryDefault("c", "--waiting--")
app.setEntryMaxLength("a", 5)
app.addButtons(["YES", "NO", "WAIT"], press)
app.addButtons(["red", "white", "green"], press)
app.addButtons(["up", "mid", "down"], press)

app.setEntryValid("a")
app.setEntryInvalid("b")
app.setEntryWaitingValidation("c")
#app.setBg("orange")

app.go()
