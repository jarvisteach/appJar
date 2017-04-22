import sys
sys.path.append("../")
from appJar import gui
#start = None

FILE_NAME = "myMap.gif"

def getit(btn=None):
    if btn is not None:
#        img = app.getGoogleMapData(location=app.getEntry("Location"), zoom=app.getScale("zoom"), imgSize="500x500", mapType=app.getOptionBox("type"))
#        app.reloadImageData("i1", img)

        app.getGoogleMapFile(FILE_NAME, location=app.getEntry("Location"), zoom=app.getScale("zoom"), imgSize="500x500", mapType=app.getOptionBox("type"))
        app.reloadImage("i1", FILE_NAME)
    else:
#        global start
#        start = app.getGoogleMapData("Marlborough, UK")
        start = app.getGoogleMapFile(FILE_NAME, "Marlborough, UK")

app=gui()
getit()
#app.addImageData("i1", start)
app.addImage("i1", FILE_NAME)
app.addLabelScale("zoom")
app.addLabelOptionBox("type", ["roadmap", "satellite", "hybrid", "terrain"])
app.setOptionBoxChangeFunction("type", getit)
app.setScaleRange("zoom", 0, 22, 18)
app.showScaleValue("zoom")
app.setScaleChangeFunction("zoom", getit)
app.addLabelEntry("Location")
app.setEntry("Location", "Swindon")
app.setEntrySubmitFunction("Location", getit)
getit()
app.go()

