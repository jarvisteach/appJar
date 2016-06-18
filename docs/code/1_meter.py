from appJar import gui

app=gui()
app.setGeometry("200x50")
app.setFont(20)
app.addMeter("progress")
app.setMeterFill("progress", "green")
app.setMeter("progress", 100, "winning")
app.go()
