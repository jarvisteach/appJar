import sys
sys.path.append("../")

from appJar import gui

app=gui()

for i in range(10):
    app.addLabel(str(i), str(i))
    app.setLabelTooltip(str(i), "stuff goes here")


app.go()
