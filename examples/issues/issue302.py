import sys
sys.path.append("../../")

def press(btn):
    if btn == "ADD":
        app.entry("file", kind="file")
    else:
        app.removeEntry("file")

from appJar import gui

app = gui()
app.addFileEntry("file")
app.addButton("REMOVE", press)
app.addButton("ADD", press)
app.go()
