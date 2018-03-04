import sys
sys.path.append("../")

from appJar import gui

app=gui("SCROLLPABE DEMO", "150x150")

app.startScrollPane("PANE")
for x in range(10):
    for y in range(10):
        name = str(x) + "-" + str(y)
        app.addLabel(name, name, row=x, column=y)
        app.setLabelBg(name, app.RANDOM_COLOUR())
app.stopScrollPane()

app.go()
