import sys
sys.path.append("../")
from appJar import gui

left = -40
right = 5

def mover():
    global left, right
    left -=5
    right += 5

    if left < -100: left = 0
    if right > 100: right = 0

    if left > right: text = "red"
    else: text = "green"
    app.setMeter("progress", [left, right], text)

app=gui()
app.setGeometry("200x50")
app.setFont(20)
app.addDualMeter("progress")
app.setMeterFill("progress", ["red", "green"])
app.setMeter("progress", [70, 30])
app.registerEvent(mover)
app.go()
