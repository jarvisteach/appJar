import sys
sys.path.append("../../")
from appJar import gui
app=gui()
app.addEmptyLabel("info")

def update(btn):
    app.setLabel("info", "some text")

app.addButton("Update", update)
app.go()
