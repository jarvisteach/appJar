from appJar import gui

def mainStop():
    print("Main sstop")
    return True

def subStop():
    print("Sub sstop")
    return True

def launch(win):
    app.showSubWindow(win)

app=gui()
app.setStopFunction(mainStop)

app.startSubWindow("one", modal=True)
app.setStopFunction(subStop)
app.addLabel("l1", "SubWindow One")
app.stopSubWindow()

app.startSubWindow("two")
#app.setStopFunction(subStop)
app.addLabel("l2", "SubWindow Two")
app.stopSubWindow()

app.addButtons(["one", "two"], launch)

app.go()
