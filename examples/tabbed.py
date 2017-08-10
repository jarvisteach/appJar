import sys
sys.path.append("../")
from appJar import gui

lid = 0
def add(btn):
    global lid
    app.openTab("book", app.getOptionBox("options"))
    app.addLabel(str(lid), str(lid))
    lid += 1

app = gui()
tp = app.startTabbedFrame("book")
app.startTab("One")
app.addLabel("l1", "stuff")
app.addOptionBox("options", ["One", "Two", "Three", "Four"])
app.addButton("add", add)
app.startTab("Two")
app.addLabel("l2", "stuff")
app.startTab("Three")
app.addLabel("l3", "stuff")
app.startTab("Four")
app.addLabel("l4", "Rename")

def press(tab):
    text = app.textBox("Text", "Text")
    app.setTabText("book", tab, text)

app.addButtons(["One", "Two", "Three", "Four"], press)

app.go()
