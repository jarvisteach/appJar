from appJar import gui

def press(btn):
    app.removeListItemAtPos("l1", app.getListItemsPos("l1")[0])

def add(btn):
    app.addListItem("l1", app.getEntry("e1"))

items=["dog", "cat", "kangaroo", "elephant", "dog", "zebra", "crocodile", "pig", "lion", "tiger", "jaguar", "puma", "dog"]

app=gui()
app.addListBox("l1", items)
app.setListBoxRows("l1",15)
app.setListSingle("l1", False)
app.addButton("DEL", press)
app.addEntry("e1")
app.addButton("ADD", add)
app.go()
