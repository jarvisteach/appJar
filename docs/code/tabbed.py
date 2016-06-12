from appJar import gui

app = gui()
app.startNoteBook("book")
app.startNoteTab("One")
app.addLabel("l1", "stuff")
app.startNoteTab("Two")
app.addLabel("l2", "stuff")
app.startNoteTab("Three")
app.addLabel("l3", "stuff")
app.startNoteTab("Four")
app.addLabel("l4", "stuff")

app.go()
