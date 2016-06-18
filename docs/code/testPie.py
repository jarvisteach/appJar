from appJar import gui

myFracs = [100,300,100, 50, 200, 60, 80, 40, 100, 20, 75, 44, 66, 88,
100,300,100, 50, 200, 60, 80, 40, 100, 20, 75, 44, 66, 88]

app=gui()
app.setBg("yellow")
app.addLabel("l1", "Title here")
app.setLabelTooltip("l1", "here")
app.addSeparator()
app.addPieChart("Details", myFracs, 30)
app.addLabel("l2", "Notes here")
app.go()
