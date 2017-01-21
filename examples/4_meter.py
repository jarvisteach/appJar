from appJar import gui

splitVal = -100
val = 0

def update():
    global val, splitVal
    val += 5
    splitVal += 5
    app.setMeter("p1", val)
    app.setMeter("p11", val, str(val))
    app.setMeter("p2", splitVal)
    app.setMeter("p3", val)
    if val == 100: val = 0
    if splitVal == 100: splitVal = -100

def show():
    print("P1:", app.getMeter("p1"))
    print("P2:", app.getMeter("p2"))
    print("P3:", app.getMeter("p3"))

app=gui()
app.setGeometry("200x150")
app.setFont(20)

app.addMeter("p1")
app.addMeter("p11")
app.addSplitMeter("p2")
app.addDualMeter("p3")

app.setMeterFill("p1", "orange")
app.setMeterFill("p2", ["orange", "purple"])
app.setMeterFill("p3", ["orange", "purple"])

app.registerEvent(update)
app.registerEvent(show)

app.go()
