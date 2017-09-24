import time
import sys
pos=0
sys.path.append("../../")

def foo():
    print("bar")

def press(e=None):
    while True:
        print("dismiss")
        time.sleep(1)

def btn(btn):
    global pos
    app.queueFunction(app.setLabel, "l1", "foo " + str(pos))
    app.queuePriorityFunction(app.setEntry, "e1", "foo", callFunction=True)
    app.queueFunction(foo)
    pos += 1

from appJar import gui
app=gui()
app.addGoogleMap("m1")

app.addLabel("l1", "empty")
app.addEntry("e1")
app.addMenuEdit(True)
app.thread(press)
app.setEntryRightClick("e1", "EDIT")
app.addButton("press", btn)
app.go()
