import time

import sys
sys.path.append("../../")
from appJar import gui

def runloop(param=None):
    for i in range(10):
        time.sleep(1)
        app.setLabel("l1", str(i))

def update_text(a=None):
    app.setLabel("l1", "Running loop")
    app.thread(runloop)

def save(btn):
    app.saveGoogleMap("g1", app.saveBox(fileExt=".gif"))

app = gui()
app.addLabel("l1", "No message")
app.addButton("Change message", update_text)
app.addGoogleMap("g1")
app.addButton("SAVE", save)
app.go()
