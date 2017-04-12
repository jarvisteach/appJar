import sys
sys.path.append("../../")
from appJar import gui

def launch(win):
        app.showSubWindow(win)

app=gui()

app.startSubWindow("Modal", modal=True, transient=True)
app.addLabel("l1", "SubWindow One")
app.addEntry("e1")
app.addButtons(["HIDE", "SHOW"], [app.hide, app.show])
app.stopSubWindow()

app.startSubWindow("unModal")
app.addLabel("l2", "SubWindow Two")
app.addEntry("e2")
app.addButtons(["HIDE2", "SHOW2"], [app.hide, app.show])
app.stopSubWindow()

app.addLabel("mt", "Modal Testing")
app.addButtons(["Modal", "unModal"], launch)

print("show popup")
launch("Modal")
print("moving on")

app.go()
