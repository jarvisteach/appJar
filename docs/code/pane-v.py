from appJar import gui

app = gui()

app.startPanedFrameVertical("p1")
app.addLabel("l1", "Inside Pane 1")

app.startPanedFrame("p2")
app.addLabel("l2", "Inside Pane 2")
app.stopPanedFrame()

app.startPanedFrame("p3")
app.addLabel("l3", "Inside Pane 3")
app.stopPanedFrame()

app.stopPanedFrame()

app.go()
