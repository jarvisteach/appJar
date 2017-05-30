import sys
sys.path.append("../../")
from appJar import gui

params=dict(imgSize="400x400")

def setParams():
    params["location"]=app.getEntry("Search:")
    params["zoom"]=app.getScale("Zoom:")
    params["mapType"]=app.getOptionBox("Type:").lower()

def getit(btn=None):
    setParams()
    app.setGoogleMap("m1", params)

def zoom(btn):
    zoom=app.getScale("Zoom:")
    if btn == "+" and zoom < 22:
        app.setScale("Zoom:", zoom + 1)
        getit()
    elif btn == "-" and zoom > 0:
        app.setScale("Zoom:", zoom - 1)
        getit()
    elif btn =="H":
        app.clearEntry("Search:")
        getit()


app=gui()
app.setLogLevel("DEBUG")

app.startLabelFrame("GoogleMaps")
app.setSticky("we")

app.addLabelEntry("Search:", colspan=2)
app.setEntrySubmitFunction("Search:", getit)

app.addGoogleMap("m1", params, colspan=2, row=1)
app.startFrame("f1", column=2, row=1)
app.addButton("H", zoom)
app.addButton("+", zoom)
app.addButton("-", zoom)
app.stopFrame()

app.addLabelScale("Zoom:", column=0, row=2)
app.setScaleRange("Zoom:", 0, 22, 16)
app.showScaleValue("Zoom:")
app.setScaleChangeFunction("Zoom:", getit)

app.addLabelOptionBox("Type:", ["Roadmap", "Satellite", "Hybrid", "Terrain"], row=2, column=1)
app.setOptionBoxChangeFunction("Type:", getit)
app.stopLabelFrame()

app.go()

