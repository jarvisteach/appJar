import sys
sys.path.append("../../")

def press(btn):
    print(btn)
    if btn == "Cols":
        print(app.colourBox())
    if btn == "dir":
        print(app.directoryBox())
    if btn == "text":
        print(app.textBox("a", "b"))
    if btn == "save":
        print(app.saveBox())

from appJar import gui
app=gui("Issue 64")
app.addMenuList("Demo", ["Help", "This", "that"], press)
app.addButton("Cols", press)
app.addButton("dir", press)
app.addButton("text", press)
app.addButton("save", press)
app.go()
