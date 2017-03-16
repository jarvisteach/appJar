import sys
sys.path.append("../")
from appJar import gui

def getScales(btn):
    print(btn)
    print("Scale", app.getScale("scale"))
    print("Scale2", app.getScale("scale2"))


app=gui()
app.setFont(20)

app.addLabelScale("scale")
app.addLabelScale("scale2")
app.addButton("GET", getScales)
app.setScaleWidth("scale", 20)
app.setScaleRange("scale2", -55,55)
app.setScaleIncrement("scale2", 3)

app.setScaleFunction("scale", getScales)

app.setLabelBg("scale", "red")
app.setLabelBg("scale2", "green")

app.showScaleValue("scale2")
app.showScaleIntervals("scale2", 10)
app.setScaleWidth("scale2", 30)
app.setScaleLength("scale2", 30)
app.go()
