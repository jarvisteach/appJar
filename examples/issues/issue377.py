import sys
sys.path.append("../../")

from appJar import gui

def getEm():
    print(app.getAllEntries())

with gui("Labels") as app:
    app.addEntry("e1")
    app.addLabelEntry("e2")
    app.entry("e3")
    app.entry("e4", label=True)
    app.entry("e5", label="New label")
    app.button("PRESS", getEm)
