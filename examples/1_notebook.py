from appJar import gui

app = gui("Notebook", useTtk=True)

app.setTtkTheme("clam")

app.startNotebook("Notebook")

app.startNote("Note 1")
app.addLabel("l1", "Note 1")
app.stopNote()

app.startNote("Note 2")
app.addLabel("l2", "Note 2")
app.stopNote()

app.startNote("Note 3")
app.addLabel("l3", "Note 3")
app.stopNote()

app.stopNotebook()

app.go()
