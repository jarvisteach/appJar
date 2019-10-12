import sys
sys.path.append("../../")

from appJar import gui

def pnt(a):
    print(a)

with gui("xx") as app:
    app.bindKey("c", pnt)
    app.bindKey("P", pnt)
    app.bindKey(",", pnt)
    app.bindKey("Key-1", pnt)

