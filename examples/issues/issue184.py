import sys
sys.path.append("../../")

def press(btn):
    print(
        app.getListItems("list1"),
        app.getListItems("list2"),
        app.getListItems("list2")
    )

from appJar import gui

app = gui()

app.addListBox("list1", ["apple", "orange", "pear", "kiwi"],0,0)
app.setListBoxGroup("list1")
app.addListBox("list2", ["apple", "orange", "pear", "kiwi"],0,1)
app.setListBoxGroup("list2")
app.addListBox("list3", ["apple", "orange", "pear", "kiwi"],0,2)
app.setListBoxGroup("list2", False)

app.addButton("CHECK", press, colspan=3)

app.go()
