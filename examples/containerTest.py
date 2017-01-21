from appJar import gui

app = gui()
app.setPadding(10,10)
#app.setBg("red")

app.addLabel("0", "This is where it starts")
app.setLabelBg("0", "white")

app.startLabelFrame("Big One")
app.setLabelFrameBg("Big One", "green")
app.addLabel("1", "This is a label")
app.setLabelPadding("1", 4, 5)
app.addLabel("2", "This is a label")
app.addLabel("3", "This is a label")
app.stopLabelFrame()

app.addLabel("10", "This is where it starts")

app.startLabelFrame("Big Two")
#app.setContainerPadding(10,10)
app.setLabelFrameBg("Big Two", "orange")
app.addLabel("4", "This is a label")
app.addLabel("5", "This is a label")
app.addLabel("6", "This is a label")
app.stopLabelFrame()

app.addLabel("11", "This is where it starts")

app.go()
