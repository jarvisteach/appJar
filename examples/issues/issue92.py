import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    print(app.getAllEntries())

app = gui("Issue 92")

for i in range(5):
    app.addLabelEntry("Entry " + str(i))
    app.setEntryDefault("Entry " + str(i), "here")

for i in range(5,10):
    app.addLabelNumericEntry("Entry " + str(i))

for i in range(10,15):
    app.addLabelSecretEntry("Entry " + str(i))

app.addButton("Show", press)

app.go()
