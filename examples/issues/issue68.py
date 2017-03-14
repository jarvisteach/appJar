import sys
sys.path.append("../../")

from appJar import gui

def pressed(btn):
    print(btn)

app=gui()
app.addButton("press me", pressed)
app.addEntry("e1")
app.enableEnter(pressed)
app.go()
