import sys
sys.path.append("../")

from appJar import gui

app=gui()
app.addLabel("l1", "DnD")
app.addEntry("dnd")
app.addTextArea("text")
app.go()
