import sys
sys.path.append("../")
from appJar import gui

app=gui()
app.setGeometry("200x50")
app.setFont(12)
app.addMeter("progress")
app.setMeterBg("progress", "lightgrey")
app.setMeterFg("progress", "gold")
app.setMeterFill("progress", "steelblue")
app.setMeter("progress", 75)
app.go()
