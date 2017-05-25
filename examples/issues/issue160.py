import sys
sys.path.append("../../")
from appJar import gui

app=gui()
app.setLogLevel("info")
app.addImage("a", "img2.gif")
app.setAnimationSpeed("a",1000)
app.go()
