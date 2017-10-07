import sys
sys.path.append("../")
from appJar import gui
def press(btn):
    app.infoBox("Info", "You clicked the link!")

app=gui()
app.setFont(20)
app.addLink("Click me", press)
app.addWebLink("appJar.info", "http://appJar.info")
app.go()
