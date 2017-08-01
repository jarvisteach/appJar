import sys
sys.path.append("../../")
from appJar import gui

app=gui()
app.addFileEntry("e1")
app.addDirectoryEntry("d1")
app.addValidationEntry("v1")
app.addButton("DEMO", None)
app.setBg("red")
app.go()
