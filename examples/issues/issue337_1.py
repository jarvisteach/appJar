import sys
sys.path.append("../../")

from appJar import gui

app = gui("appJar Testing")
#app.setStretch("none")
#app.setFont(15)
#app.setGeometry("600x400")

app.startScrollPane("sp1")
for x in range(0,40):
    label_name = "l" + str(x)
    app.addLabel(label_name, "This is inside scroll pane.")
app.stopScrollPane()

app.go()
