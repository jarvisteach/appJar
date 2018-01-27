import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
    print(btn)
    if btn == "<Up>":
        app.increaseFont()
    elif btn == "<Down>":
        app.decreaseFont()
    elif btn == "<F1>":
        app.setFont(12)

app=gui()
app.addLabel("title", "Red")
app.setBg("red")

app.bindKeys(["<Up>", "<Down>", "<Left>", "<Right>"], press)

app.bindKey("<F1>", press)
app.bindKey("<F2>", press)
app.bindKey("<F1>", press)


app.go()
