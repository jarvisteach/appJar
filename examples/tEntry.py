import sys
val=0
sys.path.append("../")
from appJar import gui
def press(btn):
    print(btn)
    print(app.getEntry("a"))
    app.setButton("Name", "b")

def num(btn):
    global val
    app.setEntry("ne1", "hiya"+str(val))
    val += 1

app=gui()
app.addEntry("a")
app.setEntryDefault("a", "This is the default")
app.setEntryMaxLength("a", 7)
app.setEntryUpperCase("a")
app.addNamedButton("Check", "Name", press)
app.addNamedButton("Check", "Name2", press)
app.addNamedButton("Check", "Name3", press)
app.addNumericEntry("ne1")
app.addButton("set", num)

app.addLink("Click Me", press)
app.addWebLink("link1", "http://www.google.com")
app.go()
