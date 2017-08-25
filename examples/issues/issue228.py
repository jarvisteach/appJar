import sys
sys.path.append("../../")
from appJar import gui

def showGmap(btn):
    app = gui()
    app.addGoogleMap("m1")
    app.setGoogleMapSize("m1", "300x500")    
    app.go()

g = gui()
g.addButton("Map", showGmap)
g.addGoogleMap("m1")
g.go()

h = gui()
h.addButton("Map", showGmap)
h.addGoogleMap("m1")
h.go()
