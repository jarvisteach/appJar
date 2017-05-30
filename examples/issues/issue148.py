import sys
sys.path.append("../../")

from appJar import gui

def mIn(btn=None):
    print("IN", btn)

def mOut(btn=None):
    print("OUT", btn)

app=gui()

app.addLabel("l1", "Label data")
app.setLabelOverFunction("l1", [mIn, mOut])

app.addButton("b1", "Button")
app.setButtonOverFunction("b1", [mIn, mOut])

app.addRadioButton("song", "song")
app.setRadioButtonOverFunction("song", [mIn, mOut])
app.addEntry("e1")
app.setEntryOverFunction("e1", [mIn, mOut])

app.go()
