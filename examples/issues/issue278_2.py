import sys
sys.path.append("../../")
from appJar import gui 

def launch(win):
    app.showSubWindow(win)

app=gui()

# this is a pop-up
app.startSubWindow("one", modal=True)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

# this is another pop-up
app.startSubWindow("two")
app.setLocation(20,20)
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

# these go in the main window
app.addButtons(["one", "two"], launch)

app.go()
