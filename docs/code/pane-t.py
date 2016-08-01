from appJar import gui

app = gui()
app.setBg("red")

app.startPanedWindow("p1")
app.setPanedWindowVertical("p1")

app.startLabelFrame("Pane 1")
app.setBg("green")
app.addLabel("l1", "Inside Pane 1")
app.stopLabelFrame()

app.startPanedWindow("p2")
app.addLabel("l2", "Inside Pane 2")

app.startPanedWindow("p3")
app.setBg("yellow")
app.addLabel("l3", "Inside Pane 3")
app.stopPanedWindow()

app.stopPanedWindow()
app.stopPanedWindow()
app.setBg("white")

app.go()
