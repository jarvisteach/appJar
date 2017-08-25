import sys
sys.path.append("../../")

from appJar import gui

def notify(btn):
    app.setLabel("l1", "Updating")
    app.after(2000, app.setLabel, "l1", "Updated message")

app=gui()
app.addLabel("l1", "Simple message here")
app.addButton("PRESS", notify)
app.go()
