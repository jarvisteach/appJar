from appJar import gui

app = gui()

app.startPanedFrame("p1")
app.addLabel("l1", "Inside Pane 1")

app.startPanedFrameVertical("p2")
app.addLabel("l2", "Inside Pane 2")

app.startPanedFrame("p3")
app.addLabel("l3", "Inside Pane 3")
app.stopPanedFrame()

app.stopPanedFrame()
app.stopPanedFrame()

app.go()
