import sys
sys.path.append("../")

def press(btn):
    if btn == "Heart":
        app.setMicroBitImage("mb", "09090:90909:90009:09090:00900")
    elif btn == "Clear":
        app.clearMicroBit("mb")
    elif btn == "Pixel":
        app.setMicroBitPixel("mb", int(app.getOptionBox("x")), int(app.getOptionBox("y")),app.getScale("Brightness") )

from appJar import gui

app=gui()
app.addMicroBit("mb", 0, 0)
app.addMicroBit("mb1", 0, 1)
app.addMicroBit("mb2", 1, 0)
app.addMicroBit("mb3", 1, 1)
app.addLabelOptionBox("x", [0,1,2,3,4], 2, 0)
app.addLabelOptionBox("y", [0,1,2,3,4], 2, 1)
app.addLabelScale("Brightness", colspan=2)
app.setScaleRange("Brightness", 1, 9)
app.showScaleValue("Brightness")
app.addButtons(["Heart", "Clear", "Pixel"], press, colspan=2)
app.go()
