import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    app.setBg(app.getEntry("Colour"))
    app.setPieChart("p1", app.getEntry("Name"), app.getEntry("Amount"))

def test(btn):
    if btn =="HIDE":
        app.hidePieChart("p1")
    elif btn =="SHOW":
        app.showPieChart("p1")
    elif btn =="REMOVE":
        app.removePieChart("p1")

app=gui()
app.setBg("grey")
#app.addPieChart("p1", [50, 200, 75, 300, 150], size=300)
app.addPieChart("p1", {"apples":50, "oanges":200, "grapes":75,
                        "beef":300, "turkey":150})
#app.addLabelEntry("Name")
#app.addLabelNumericEntry("Amount")
#app.addLabelEntry("Colour")
#app.addButton("PRESS", press)
#app.setButtonTooltip("PRESS", "help me")
#
#app.addButtons(["HIDE", "SHOW", "REMOVE"], test)
app.go()
