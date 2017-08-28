import sys
sys.path.append("../../")

from appJar import gui
app = gui()
app.useTtk()
app.startNotebook("notes")

app.startNote("Note 1")
app.addLabel("ll1", "Example")
app.addLabel("ll2", "Example")
app.addLabel("ll3", "Example")
app.addLabel("ll4", "Example")
app.addLabel("ll5", "Example")
app.stopNote()

app.startNote("Note 2")
app.addLabel("l2", "Example")
app.stopNote()

app.startNote("Note 3")
app.addLabel("l3", "Example")
app.stopNote()

app.startNote("Note 4")
app.addLabel("l4", "Example")
app.stopNote()
app.stopNotebook()
app.go()
