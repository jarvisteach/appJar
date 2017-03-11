import sys
sys.path.append("../")
from appJar import gui

val=0

def up(btn=None):
    global val
    val += 5
    if val == 100: val = 0

    app.setMeter("progress", val)
    print(val)

app=gui()
app.setGeometry("200x50")
app.setFont(20)
app.addSplitMeter("progress")
app.setMeterFill("progress", ["green", "red"])
app.setMeter("progress", 75)
#app.registerEvent(up)
app.go()
