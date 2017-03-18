import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "Hide": app.hide()
    elif btn == "Show": app.show()
    else: app.showSubWindow(btn)

app=gui("Window")

app.startSubWindow("Menu")
app.addButton("Hide", press)
app.addButton("Show", press)
app.stopSubWindow()

for loop in range(5):
    label = "PopUp" + str(loop)
    app.startSubWindow(label)
    app.setLocation(100+loop*100, 100)
    app.addLabel(label, label)
    app.openSubWindow("Menu")
    app.addButton(label, press)
    app.stopSubWindow()
    app.addGrip()
    app.stopSubWindow()


app.addLabel("l1", "mmmmmmmmmm")
app.addButton("Menu", press)
#app.go(startWindow="Menu")
app.go()
