import sys
sys.path.append("../../")

from appJar import gui

def entered(btn):
    print("entered", btn)

def buttoned(btn):
    print("buttoned", btn)

app=gui()
app.addButton("press me", buttoned)
app.addEntry("e1")
app.enableEnter(entered)
app.go()
