import sys
sys.path.append("../../")
from appJar import gui

def caller(event=None):
    print(event)

def get(btn):
    if btn == "GET":
        print(app.getOptionBox("Favourite Pets"))
    elif btn == "CLEAR":
        app.clearOptionBox("Favourite Pets", callFunction=app.getCheckBox("OPTION - call"))
    elif btn == "ALL":
        app.clearAllOptionBoxes(callFunction=app.getCheckBox("OPTION - call"))
    elif btn == "DEL":
        app.deleteOptionBox("pp", "Fish")
        app.deleteOptionBox("Favourite Pets", "Fish")
    elif btn == "RENAME":
        print("renaming")
        app.setOptionBox("pp", app.getOptionBox("pp"), callFunction=app.getEntry("e1"))
#        app.setOptionBox("Favourite Pets", "Fish")

def press(btn):
    if btn == "OPTION":
        app.setOptionBox("pp", 1, callFunction=app.getCheckBox("OPTION - call"))
    elif btn == "TICKS":
        app.setOptionBox("Favourite Pets", "Hamsters", True, callFunction=app.getCheckBox("TICKS - call"))

app=gui()
app.setFont(20)

app.addOptionBox("pp", ["-pp-", "Dogs", "Cats", "Hamsters", "Fish"])
app.addTickOptionBox("Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"])

app.setOptionBoxChangeFunction("pp", caller)
app.setOptionBoxChangeFunction("Favourite Pets", caller)

app.addButtons(["RENAME", "GET", "CLEAR", "ALL", "DEL"], get)
app.addEntry("e1")
app.addCheckBox("OPTION - call")
app.addCheckBox("TICKS - call")

app.setCheckBox("OPTION - call")
app.setCheckBox("TICKS - call")

app.addButtons(["OPTION", "TICKS"], press)

app.go()
