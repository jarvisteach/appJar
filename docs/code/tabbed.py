from appJar import gui

app = gui()
app.startTabbedFrame("book")
app.startTab("One")
app.addLabel("l1", "stuff")
app.startTab("Two")
app.addLabel("l2", "stuff")
app.startTab("Three")
app.addLabel("l3", "stuff")
app.startTab("Four")
app.addLabel("l4", "stuff")

app.go()
