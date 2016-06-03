from rwbatools import gui

def press(btn):
    app.removeListItem("l1", app.getListItems("l1")[0])

def add(btn):
    app.addListItem("l1", [app.getEntry("e1")])

items=["dog", "cat", "kangaroo", "elephant", "zebra", "crocodile", "pig", "lion", "tiger", "jaguar", "puma"]

app=gui()
app.addListBox("l1", items)
app.addButton("DEL", press)
app.addEntry("e1")
app.addButton("ADD", add)
app.go()
