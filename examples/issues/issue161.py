import sys
sys.path.append("../../")
from appJar import gui
def showCB(btn=None):
    print(app.getCheckBox("cb1"))
    print(app.getCheckBox("cb2"))
    print(app.getCheckBox("cb3"))
    print(app.getCheckBox("cb4"))
    print(app.getCheckBox("cb5"))

app=gui()
print(app.SHOW_VERSION())
app.addNamedCheckBox("fred", "cb1")
app.addNamedCheckBox("fred", "cb2")
app.addNamedCheckBox("fred", "cb3")
app.addNamedCheckBox("fred", "cb4")
app.addNamedCheckBox("fred", "cb5")
app.addButton("PRESS", showCB)
app.go()
