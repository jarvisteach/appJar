from appJar import gui

app=gui()
app.setGeometry("200x50")
app.setFont(20)
app.addSplitMeter("progress")
#app.setMeterFill("progress", "green")
app.setMeter("progress", -70)
app.go()
