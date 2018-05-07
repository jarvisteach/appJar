import sys
sys.path.append("../../")
from appJar import gui
def keyPress(key):
    if key == "<Up>":
        app.increaseFont()
    elif key == "<Down>":
        app.decreaseFont()

app = gui("Button Demo")
app.addLabel("title", "Press the arrow keys to change the font")
app.bindKey("<Up>", keyPress)
app.bindKey("<Down>", keyPress)
app.go()
