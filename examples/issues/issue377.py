import sys
sys.path.append("../../")

from appJar import gui

def getEm():
    print(app.getAllEntries())

def getEmi(btn):
    print(btn)
    print(app.getAllEntries())

with gui("Labels") as app:
    app.addEntry("e1")
    app.addLabelEntry("e2")
    app.entry("e3")
    app.entry("e4", label=True)
    app.entry("e5", label="New label")
    app.button("PRESS", getEm)
    app.button("PRESS2", getEmi, name="PRESS")
    app.link("click me", getEm)
    app.link("click me2", getEmi)
    app.bindKey("z", getEm)
    app.bindKey("x", getEmi)
