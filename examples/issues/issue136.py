import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    if btn == "SEARCH": 
        app.searchGoogleMap("m1", app.getEntry("e1"))
    elif btn == "ZOOM": 
        app.zoomGoogleMap("m1", int(app.getEntry("e1")))
    elif btn == "TERRAIN": 
        app.setGoogleMapTerrain("m1", app.getEntry("e1"))
    elif btn == "SIZE": 
        app.setGoogleMapSize("m1", app.getEntry("e1"))
    elif btn == "MARK": 
        app.setGoogleMapMarker("m1", app.getEntry("e1"))
    elif btn == "SAVE": 
        app.saveGoogleMap("m1", app.getEntry("e1"))
    else:
        app.zoomGoogleMap("m1", btn)
        

app=gui()
app.setLogLevel("DEBUG")
app.addGoogleMap("m1")
app.setGoogleMapMarker("m1", "swindon")
app.setGoogleMapSize("m1", "340x500")
app.addEntry("e1")
app.addButtons(["SAVE", "SEARCH", "+", "-", "ZOOM", "SIZE", "TERRAIN", "MARK"], press)

app.go()

