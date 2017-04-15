import sys
sys.path.append("../")

from appJar import gui

def here(data):
    print(data)

app=gui()
app.addLabel("l1", "DnD")
app.addEntry("dnd")
app.setEntryDndFunction("dnd", here)
app.addTextArea("text")
app.setTextAreaDndFunction("text", here)
app.go()
