import sys
sys.path.append("../../")
from appJar import gui

def press(): pass

app = gui()
app.addFileEntry("fe1")
app.addLabel("hello", "hello")
app.setLabelBg('hello', 'red')
app.setLabelHeight('hello', 17)
app.setEntryAlign("fe1", 'right')
app.setEntryAnchor("fe1", 'e')
app.setEntryWidth("fe1", 40)
app.setEntryHeight("fe1", 7)
app.go()
