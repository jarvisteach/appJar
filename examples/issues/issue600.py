import sys
sys.path.append("../../")

from appJar import gui

def externalDrop(data):
    print("Data dropped:", data)

app = gui("External dnd Demo")

app.setFont(20)
app.setBg("SlateGrey")
app.setFg("yellow")

app.addLabel("dropLab", "Drop Here")
app.setLabelDropTarget("dropLab", externalDrop)

app.go()
