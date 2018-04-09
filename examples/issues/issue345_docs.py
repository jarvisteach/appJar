import sys
sys.path.append("../../")

from appJar import gui 

def press(btn):
    if btn == "FIRST": app.firstFrame("Pages")
    elif btn == "NEXT": app.nextFrame("Pages")
    elif btn == "PREV": app.prevFrame("Pages")
    elif btn == "LAST": app.lastFrame("Pages")

app=gui("FRAME STACK")

app.startFrameStack("Pages", start=1)

app.startFrame()
for i in range(5):
    app.addLabel("Text: " + str(i))
app.stopFrame()

app.startFrame()
for i in range(5):
    app.addEntry("e" + str(i))
app.stopFrame()

app.startFrame()
for i in range(5):
    app.addButton(str(i), None)
app.stopFrame()

app.stopFrameStack()

app.addButtons(["FIRST", "PREV", "NEXT", "LAST"], press)
app.go()
