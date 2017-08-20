import sys
sys.path.append("../../")

def press(btn):
    print(btn)
    app.okBox("OK", "EMPTY")

from appJar import gui

app=gui()
app.addLabel("l1", "DEFAULT")
app.addLabel("l2", "DEFAULT")
app.addLabel("l3", "DEFAULT")
#app.translations["POPUP"]["OK"]=["Confirmation", "Press the button"]


app.addButton("PRESS", press)
app.go("ENGLISH")
