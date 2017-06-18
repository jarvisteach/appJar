import sys
sys.path.append("../../")

from appJar import gui

app=gui()

app.addLabel("Vertical", "Vertical limit:", 2, 2, 1)
app.addValidationEntry("Vertical_e", 2, 3)
app.setEntry("Vertical_e", "75")
app.setEntryWidth("Vertical_e", 2)
#app.getLabelWidget("Vertical_e").entry.config(width=2)

app.go()
