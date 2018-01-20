import sys
sys.path.append("../")
from appJar import gui

def press(a=None):
    print("double")

with gui("List Test") as app:
#    l = app.list("l1", [1, 2, 3, 4, 5])
    l = app.addListBox("l1", [1, 2, 3, 4, 5])
    l.bind("<Double-1>", lambda *args: press())
