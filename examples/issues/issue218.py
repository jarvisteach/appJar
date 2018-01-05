import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    app.setEntry("ne1", app.getEntry("e1"))
    app.setEntry("t1", app.getEntry("e1"))

with gui() as app:
    app.addNumericEntry("ne1")
    app.addEntry("t1")
    app.addEntry("e1")
    app.addButton("COPY", press)
