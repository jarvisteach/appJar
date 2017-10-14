import sys
sys.path.append("../")
from appJar import gui

app=gui()

app.startFrame("f1", 0, 0)
app.setBg("purple")
app.addLabel("a", "a")
app.addLabel("b", "b")
app.addLabel("c", "c")
app.stopFrame()

app.startFrame("f2", 0, 1)
app.addLabel("d", "d")
app.addLabel("e", "e")
app.addLabel("f", "f")
app.stopFrame()

app.setFrameBg("f2", "yellow")
app.setFrameTooltip("f1", "help me")

app.go()
