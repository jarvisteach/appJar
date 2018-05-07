import sys
sys.path.append("../")

from appJar import gui

def press(btn):
    app.setLanguage(btn)

app=gui()

for i in range(10):
    app.addLabel("l"+str(i), str(i))
    app.setLabelTooltip("l"+str(i), "stuff goes here")

app.addEntry("e1")
app.setEntryTooltip("e1", "some tooltips")
app.addEntry("no tooltip")

app.addButton("FRENCH", press)
app.setButtonTooltip("FRENCH", "click here to change language")
app.go()
