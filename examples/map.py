import sys
sys.path.append("../")

from appJar import gui
app=gui()
app.addGoogleMap("gq")
app.go()
