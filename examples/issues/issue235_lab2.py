import sys
sys.path.append("../../")
from appJar import gui

with gui("Grid Demo", "300x300") as app:
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(size=14)

    app.label("l1", "row=0\ncolumn=0", bg="red")
    app.label("l2", "row=0\ncolumn=1\ncolspan=2", pos=(0, 1, 2), bg="blue")
    app.label("l4", "row=1\ncolumn=0\ncolspan=2", pos=(1, 0, 2), bg="green")
    app.label("l6", "row=1\ncolumn=2\ncolspan=1\nrowspan=2", pos=(1, 2, 1, 2), bg="orange")
    app.label("l7", "row=2\ncolumn=0", pos=(2), bg="yellow")
    app.label("l8", "row=2\ncolumn=1", pos=(2, 1))
