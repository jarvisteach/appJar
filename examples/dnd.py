import sys
sys.path.append("../")

from appJar import gui

def here(data):
    print(data)
    return("here")

app=gui()
app.addLabel("l1", "DnD")

app.addEntry("dnd")
app.setEntryDropTarget("dnd", None, replace=False)

app.addListBox("l1", [])
app.setListBoxDropTarget("l1")

app.addMessage("m1", "lots of message text...")
app.setMessageDragSource("m1", function=here)

app.addTextArea("text")
app.setTextAreaDropTarget("text", None)

app.addScrolledTextArea("text2a")
app.setTextAreaDropTarget("text2a", None)

app.addImage("m1", "images/balloons.gif")
app.setImageDropTarget("m1", None)

app.addLabel("im1", "try here...")
app.setLabelDropTarget("im1", None)
app.go()
