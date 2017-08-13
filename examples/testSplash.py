import sys
sys.path.append("../")

from appJar import gui

app=gui()
app.showSplash()
app.addLabel("l1", "hiya")
app.go()
