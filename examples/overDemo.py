import sys
sys.path.append("../")
from appJar import gui

def enter(wdgt): 
    app.setLabel("l1", "IN")
def leave(wdgt):
    app.setLabel("l1", "OUT")

app=gui("LabelDemo", "300x300")
app.setBg("blue")
app.addLabel("l1", "Testing...")
app.setLabelBg("l1", "yellow")
app.setLabelWidth("l1", 20)
app.setLabelHeight("l1", 20)
app.setLabelOverFunction("l1", [enter, leave])
app.go()
