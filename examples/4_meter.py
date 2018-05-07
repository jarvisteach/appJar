import sys
sys.path.append("../")
from appJar import gui

val = 0
dualVal = [-75, 30]

def update():
    global val, dualVal
    val += 5
    dualVal[0] = dualVal[0] - 5
    dualVal[1] = dualVal[1] + 5
    app.setMeter("p1", val)
    app.setMeter("p11", val, str(val))
    app.setMeter("p2", val, "bigger")
    app.setMeter("p3", dualVal)
    if val == 120: val = 0
    if dualVal[0] < -100: dualVal[0] = 0
    if dualVal[1] > 100: dualVal[1] = 0

def show():
    print("P1:", app.getMeter("p1"))
    print("P2:", app.getMeter("p2"))
    print("P3:", app.getMeter("p3"))

app=gui()
#app.setGeometry("200x150")
app.setFont(20)

app.addLabel("l1", "Meter - default set")
app.addMeter("p1")
app.addLabel("l2", "Meter - string set")
app.addMeter("p11")
app.addLabel("l3", "Split Meter 2 vals")
app.addSplitMeter("p2")
app.addLabel("l4", "Dual Meter")
app.addDualMeter("p3")

app.setMeterFill("p1", "pink")
app.setMeterFill("p11", "black")
app.setMeterFill("p2", ["green", "red"])
app.setMeterFill("p3", ["orange", "purple"])

app.setMeterBg("p1", "grey")
app.setMeterBg("p11", "grey")
app.setMeterBg("p2", "grey")
app.setMeterBg("p3", "grey")

app.setMeterFg("p1", "orange")
app.setMeterFg("p11", "yellow")
app.setMeterFg("p2", "grey")
app.setMeterFg("p3", "lightblue")

app.registerEvent(update)
app.registerEvent(show)

app.go()
