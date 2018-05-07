import sys
sys.path.append("..")
from appJar import gui

def press(btn):
    text = app.textBox("New title", "Enter a new title:")
    app.setLabelFrameTitle("Songs", text)

def setAnchor(anchor):
    app.setLabelFrameAnchor("Songs", anchor.lower())

app = gui()
app.addLabel("header", "The header")
app.startLabelFrame("Songs")
app.addRadioButton("song", "Song 1")
app.addRadioButton("song", "Song 2")
app.addRadioButton("song", "Song 3")
app.addRadioButton("song", "Song 4")
app.stopLabelFrame()

app.addButton("CHANGE", press)
app.addButtons(["NW", "NE", "SW", "SE"], setAnchor)

app.startSubWindow("empty")
app.addLabel("el", "Empty Sub")
app.stopSubWindow()

app.showSubWindow("empty")

app.go()
