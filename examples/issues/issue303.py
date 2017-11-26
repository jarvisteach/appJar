import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    print(btn)
    if btn == "<Up>":
        app.increaseFont()
    else:
        app.decreaseFont()

app=gui()
app.addLabel("title", "Red")
app.setBg("red")

app.bindKeys(["<Up>", "<Down>", "<Left>", "<Right>"], press)

app.bindKey("<F1>", press)
app.bindKey("<F2>", press)

app.go()
