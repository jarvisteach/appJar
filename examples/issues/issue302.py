import sys
sys.path.append("../../")

def press(btn):
    if btn == "ADD":
        app.entry("file", kind="file")
    else:
        app.removeEntry("file")

from appJar import gui

with gui() as app:
    app.entry("file", kind="file")
    app.button("REMOVE", press)
    app.button("ADD", press)
