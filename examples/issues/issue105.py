import sys
sys.path.append("../")
from appJar import gui

app=gui()
app.setBg("crimson")
app.addLabel("L1", "red")
app.go()
