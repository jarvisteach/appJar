import sys
sys.path.append("../../")
from appJar import gui

app=gui()
app.setLogLevel("DEBUG")
app.addGoogleMap("m1")

app.go()

