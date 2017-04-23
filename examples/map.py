import sys
sys.path.append("../")
from appJar import gui
#start = None

FILE_NAME = "myMap.gif"

def getit(btn=None):
    if btn is not None:
        location=app.getEntry("Search:")
        zoom=app.getScale("Zoom:")
        imgSize="500x500"
        mapType=app.getOptionBox("Type:").lower()
        
        #img = app.getGoogleMapData(location=location, zoom=zoom, imgSize=imgSize, mapType=mapType)
        img = app.getGoogleMapFile(FILE_NAME, location=location, zoom=zoom, imgSize=imgSize, mapType=mapType)

        if img is not None:
#            app.reloadImageData("i1", img)
            app.reloadImage("i1", FILE_NAME)
        else:
            app.errorBox("Error", "Failed to contact GoogleMaps")

    else:
#        global start
#        start = app.getGoogleMapData(location)
        start = app.getGoogleMapFile(FILE_NAME)
        if start is None:
            app.error("Unable to contact google maps")


app=gui()
getit()

app.addLabelEntry("Search:", colspan=2)
app.setEntrySubmitFunction("Search:", getit)

app.startLabelFrame("GoogleMaps", colspan=2)
#app.addImageData("i1", start)
app.addImage("i1", FILE_NAME)
app.stopLabelFrame()

app.addLabelScale("Zoom:", column=0, row=2)
app.setScaleRange("Zoom:", 0, 22, 16)
app.showScaleValue("Zoom:")
app.setScaleChangeFunction("Zoom:", getit)

app.addLabelOptionBox("Type:", ["Roadmap", "Satellite", "Hybrid", "Terrain"], row=2, column=1)
app.setOptionBoxChangeFunction("Type:", getit)

app.go()

