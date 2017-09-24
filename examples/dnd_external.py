import sys
sys.path.append("../")

from appJar import gui

def drag(widget):
    app.info("Dragged from:" + str(widget))

def drop(widget):
    app.info("Dropped on:" + str(widget))

def externalDrop(data):
    app.info("External drop:" + str(data))

app = gui("dnd Demo")

app.setFont(20)
app.setBg("SlateGrey")
app.setFg("yellow")
app.debug("configued bits")
app.addTooltip("aa", a="a")

app.addLabel("dragLab", "Drag Me")
app.enableLabelTooltip("dragLab")
app.setLabelTooltip("dragLab", "Drag me to initiate a DnD drag event.")
app.setLabelTooltip("dragLab", "Drag me to initiate a DnD drag event.")
app.addHorizontalSeparator()
app.addLabel("dropLab", "Drop Here")
app.setLabelTooltip("dropLab", "Try dropping stuff on me - from anywhere!")
app.setLabelTooltip("dropLab", "")
app.setLabelTooltip("dropLab", None)
app.setLabelTooltip("dropLab", "No, I really mean it!!!")
app.addLabelTooltip("dropLab")
app.debug("added widgets")

app.setLabelDragFunction("dragLab", [drag, drop])
app.setLabelDropTarget("dropLab", externalDrop)
app.debug("setup dnd")

app.go()
