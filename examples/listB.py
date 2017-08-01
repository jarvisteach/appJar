import sys
sys.path.append("../")
from appJar import gui

def press(btn):
    listName = app.getFocus()
    if listName is not None: app.removeListItemAtPos(listName, app.getListItemsPos(listName)[0])

def add(btn):
    app.addListItem("l1", app.getEntry("e1"))

items=["dog", "cat", "kangaroo", "elephant", "dog", "zebra", "crocodile", "pig", "lion", "tiger", "jaguar", "puma", "dog"]

app=gui()
app.addListBox("l1", items, 0, 0)
app.addListBox("l2", items, 0, 1)
app.setListBoxRows("l1",15)
app.setListBoxMulti("l1")
app.addButton("DEL", press)
app.addEntry("e1")
app.addButton("ADD", add)
app.setEntryFocus("e1")
app.go()
