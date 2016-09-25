from appJar import gui

app=gui("NoteBook Demo", "200x200")

app.startTabbedFrame("nb")
app.startTab("One")
app.addLabel("l1", "Tab One")
app.stopTab()
app.startTab("Two")
app.addLabel("l2", "Tab Two")
app.stopTab()
app.startTab("Three")
app.addLabel("l3", "Tab Three")
app.stopTab()
app.stopTabbedFrame()
app.go()
