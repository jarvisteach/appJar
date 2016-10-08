from appJar import gui

def checkDone():
    return True

def launch(win):
    if win == "one": app.showSubWindow("one")
    elif win == "two": app.showSubWindow("two")
    elif win == "three": app.showSubWindow("three")
    elif win == "four": app.showSubWindow("four")
    elif win == "in": app.showSubWindow("inner")

app=gui()
app.setLocation(100,100)

app.addButtons(["one", "two", "three", "four"], launch)

app.startSubWindow("one", modal=True)
app.setBg("orange")
app.setGeometry("400x400")
app.setStopFunction(checkDone)
app.addLabel("l1", "In sub window - MODAL")
app.stopSubWindow()

app.startSubWindow("two")
app.setGeometry("fullscreen")
app.addLabel("l2", "Sub Window two - FULLSCREEN")
app.stopSubWindow()

app.startSubWindow("three")
app.setTransparency(50)
app.addLabel("l3", "Sub Window three - TRANSPARENCY")
app.stopSubWindow()

app.startSubWindow("four")
app.setLocation(900,900)
app.addLabel("l4", "Sub Window four - LOCATION")
app.stopSubWindow()

app.go()
