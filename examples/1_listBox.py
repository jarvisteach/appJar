import sys
sys.path.append("../")

from appJar import gui
def press(btn):
    items = app.getListItems("list")
    print(items)
    if len(items)> 0:
        app.removeListItem("list", items[0])

app=gui()
app.setFont(20)
app.addListBox("list", ["apple", "orange", "pear", "kiwi"])
app.setListBoxMulti("list")
app.selectListItem("list", "apple")
app.selectListItem("list", "pear")
app.addButton("press",  press)
app.go()
