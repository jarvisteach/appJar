import sys
sys.path.append("../../")
from appJar import gui
app = gui()
app.addFileEntry("e1").theButton.config(text='hello')
fe = app.addFileEntry("e2")
fe.theButton.config(text='hello')

app.setEntryDefault("e1", "new default")

app.go()
