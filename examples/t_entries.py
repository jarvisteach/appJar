import sys
sys.path.append("../")
from appJar import gui

app=gui()
app.setFont(20)

app.addEntry("e1")
app.addEntry("e2")
app.addEntry("e3")
app.addLabelEntry("Name")
app.addValidationEntry("v1")
app.addFileEntry("f1")

app.setEntryDefault("e2", "Age here")
app.setEntryValid("v1")

app.go()

