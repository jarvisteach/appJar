import sys
sys.path.append("../../")
from appJar import gui

def get(btn):
    if btn == "GET": print(app.getOptionBox("Favourite Pets"))
    elif btn == "CLEAR": app.clearOptionBox("Favourite Pets")
    elif btn == "ALL": app.clearAllOptionBoxes()
    elif btn == "DEL":
        app.deleteOptionBox("pp", "Fish")
        app.deleteOptionBox("Favourite Pets", "Fish")

app=gui()
app.setFont(20)
app.addOptionBox("pp", ["-pp-", "Dogs", "Cats", "Hamsters", "Fish"])
app.addTickOptionBox("Favourite Pets", ["Dogs", "Cats", "Hamsters", "Fish"])
app.addButtons(["GET", "CLEAR", "ALL", "DEL"], get)
app.go()
