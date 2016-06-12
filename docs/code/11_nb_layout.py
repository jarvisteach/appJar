from appJar import gui

app=gui("NoteBook Demo", "200x200")

app.startNoteBook("nb")
app.startNoteTab("One")
app.addLabel("l1", "Tab One")
app.stopNoteTab()
app.startNoteTab("Two")
app.addLabel("l2", "Tab Two")
app.stopNoteTab()
app.startNoteTab("Three")
app.addLabel("l3", "Tab Three")
app.stopNoteTab()
app.stopNoteBook()
app.go()
