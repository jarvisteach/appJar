import sys
sys.path.append("../../")

from appJar import gui
win = 'one'

def launch(win):
    app.startSubWindow(win, modal=True)
    app.addLabelEntry("Window one") #LabeledEntry considered as duplicate
    app.addButton("close window", destroyWindow)
    app.stopSubWindow()
    app.showSubWindow(win)

def destroyWindow(btn):
    app.destroySubWindow("one")

app=gui()
app.setSize(400, 600)
app.setSticky("nw")
app.startFrame("LEFT", row=0, column=0)
app.addButton("one", launch)
app.stopFrame()
app.go()
