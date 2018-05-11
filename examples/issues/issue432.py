import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn == "ONE": frame1.lift()
    elif btn == "TWO": frame2.lift()

app = gui()
frame1 = app.startFrame("Frame 1", 0, 0)
app.addLabel("In frame one")
app.stopFrame()
frame2 = app.startFrame("Frame 2", 0, 0)
app.addLabel("In frame two")
app.stopFrame()
app.addButtons(["ONE", "TWO"], press)
app.go()
