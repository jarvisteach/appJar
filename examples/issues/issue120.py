import time

import sys
sys.path.append("../../")
from appJar import gui

def runloop(param=None, other=None):
    for i in range(100):
        time.sleep(1)
        print(other)
        app.queueFunction(app.setLabel, "l1", param+str(i))

def update_text(a=None):
    app.setLabel("l1", "Running loop")
    app.thread(runloop, "fred", other="aaa")

def save(btn):
    app.saveGoogleMap("g1", app.saveBox(fileExt=".gif"))

app = gui()
app.addLabel("l1", "No message")
app.addButton("Change message", update_text)
app.addGoogleMap("g1")
app.addButton("SAVE", save)
app.go()
