import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "SUB":
        app.hide()
        app.showSubWindow("Sub Window")
    elif btn == "MAIN":
        app.show()
        app.hideSubWindow("Sub Window")
    elif btn in ["EXIT", "e"]:
        app.stop()

def mainStop(btn=None):
    print("Main stop")
    return True

def subStop(btn=None):
    app.show()
    return True


app=gui("Main Window")

app.addLabel("title", "Main Window")
app.addButton("SUB", press)
app.addButton("EXIT", press)
app.setStopFunction(mainStop)

app.startSubWindow("Sub Window")
app.addLabel("sub_title", "Sub Window")
app.addButton("MAIN", press)
app.addNamedButton("EXIT", "e", press)
app.setStopFunction(subStop)
app.stopSubWindow()



app.go()
