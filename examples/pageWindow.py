import sys
sys.path.append("../")
from appJar import gui

lid = 0
def add(btn):
    global lid
    app.openPage("Main Title", app.getSpinBox("spin"))
    app.addLabel(str(lid), str(lid))
    lid +=1
    app.stopPage()

app=gui()

app.setBg("DarkKhaki")
app.setGeometry(280,400)

app.startPagedWindow("Main Title")

app.startPage()
app.addLabel("l13", "Label 1")
app.addSpinBoxRange("spin", 1, 5)
app.addButton("addLabel", add)
app.stopPage()

app.startPage()
app.stopPage()

app.startPage()
app.addLabel("l3", "Label 3")
app.stopPage()

app.startPage()
app.addLabel("l4", "Label 4")
app.stopPage()

app.stopPagedWindow()
app.go()
