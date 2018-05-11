import sys
sys.path.append("../../")
from appJar import gui

def launch():
    app.startSubWindow("onet", modal=True)
    app.setBg("orange")
#    app.setGeometry("400x400")
    #app.setTransparency(25)
    #app.setStopFunction(checkDone)
    app.addLabel("l1", "In sub window")
    app.stopSubWindow()
    app.showSubWindow("onet")


app=gui()

# these go in the main window
app.addButtons(["one"], launch)

# this is a pop-up
# app.startSubWindow("one", modal=True)
# app.addLabel("l1", "SubWindow One")
# app.stopSubWindow()

# this is another pop-up

app.startSubWindow("PopUp")
app.addLabel("SubWindow")
app.stopSubWindow()

app.showSubWindow('PopUp')

app.go()
