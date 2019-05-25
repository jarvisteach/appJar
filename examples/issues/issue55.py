import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.setSticky("news")
    app.setExpand("both")
    app.setFont(14)

    app.addLabel("l1", "row=0\ncolumn=0")
    app.colspan=2
    app.addLabel("l2", "row=0\ncolumn=1\ncolspan=2", 0, 1)
    app.addLabel("l4", "row=1\ncolumn=0\ncolspan=2", 1, 0)
    app.config(colspan=0, rowspan=2)
    app.addLabel("l6", "row=1\ncolumn=2\ncolspan=1\nrowspan=2", 1, 2)
    app.addLabel("l7", "row=2\ncolumn=0", 2, rowspan=1)
    app.addLabel("l8", "row=2\ncolumn=1", 2, 1)

    app.setLabelBg("l1", "red")
    app.setLabelBg("l2", "blue")
    app.setLabelBg("l4", "green")
    app.setLabelBg("l6", "orange")
    app.setLabelBg("l7", "yellow")
