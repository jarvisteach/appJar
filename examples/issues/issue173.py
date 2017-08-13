import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
   newVal = app.getEntry("en1")
   item = app.getListBox("list")[0]
   app.setListItem("list", item, newVal)
   app.setListItemBg("list", newVal, "green")


app=gui()

app.addListBox("list", ["apple", "orange", "pear", "kiwi"])
app.addEntry("en1")
app.addButton("PRESS", press)

app.go()
