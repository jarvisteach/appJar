import sys
sys.path.append("../")
from appJar import gui
def press(btn):
    print(btn)
    print(app.getEntry("a"))
    app.setButton("Check", "b")
app=gui()
app.addEntry("a")
app.setEntryDefault("a", "This is the default")
app.setEntryMaxLength("a", 7)
app.setEntryUpperCase("a")
app.addnamedButton("Check", "Name", press)
app.addNamedButton("Check", "Name2", press)
app.addNamedButton("Check", "Name3", press)

app.addLink("Click Me", press)
app.addWebLink("link1", "http://www.google.com")
app.go()
