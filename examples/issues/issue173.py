import sys
sys.path.append("../../")
from appJar import gui

def press(btn):
   item = app.getListItems("list")[0]
   app.setListItemBg("list", item, "green")
   newVal = app.getEntry("en1")
   app.setListItem("list", item, newVal)


app=gui()

app.addListBox("list", ["apple", "orange", "pear", "kiwi"])
app.addEntry("en1")
app.addButton("PRESS", press)

app.go()
