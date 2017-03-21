import sys
sys.path.append("../")

from appJar import gui

def mIn(btn):
    print("Mouse in:", btn)

def mOut(btn):
    print("Mouse out:", btn)

def sDrag(btn):
    print("sDrag:", btn)

def eDrag(btn):
    print("eDrag:", btn)

app = gui("Event 2")
app.setFont(20)
app.addLabel("l1", "Label 1", 0, 0)
app.addLabel("l2", "Label 2", 0, 1)
app.addLabel("l3", "Label 3", 1, 0)
app.addLabel("l4", "Label 4", 1, 1)


app.setLabelOverFunction("l1", [mIn, mOut])
app.setLabelDragFunction("l1", [sDrag, eDrag])

app.go()
