import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "Grouped":
        app.showSubWindow("Grouped")
    elif btn == "Not-grouped":
        app.showSubWindow("Not Grouped")

app=gui("Main Window")
app.addLabel("l1", "Main Window")
app.addButtons(["Grouped", "Not-grouped"], press)

app.startSubWindow("Grouped", transient=True)
app.addLabel("g1", "Grouped")
app.stopSubWindow()

app.startSubWindow("Not Grouped", grouped=False, transient=True)
app.addLabel("g2", "Not Grouped")
app.stopSubWindow()


app.go()
