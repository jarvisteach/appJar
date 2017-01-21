from appJar import gui
def press(btn):
    items = app.getListItems("list")
    if len(items)> 0:
        app.removeListItem("list", items[0])

app=gui()
app.setFont(20)
app.addListBox("list", ["apple", "orange", "pear", "kiwi"])
app.addButton("press",  press)
app.go()
