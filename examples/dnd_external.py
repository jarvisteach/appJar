import sys
sys.path.append("../")

from appJar import gui

def drag(widget):
    print("Dragged from:", widget)

def drop(widget):
    print("Dropped on:", widget)

def externalDrop(data):
    print("External drop:", data)

app = gui("dnd Demo")

app.setFont(20)
app.setBg("SlateGrey")
app.setFg("yellow")

app.addLabel("dragLab", "Drag Me")
app.addHorizontalSeparator()
app.addLabel("dropLab", "Drop Here")

app.setLabelDragFunction("dragLab", [drag, drop])
app.setLabelDropTarget("dropLab", externalDrop)

app.go()
