import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:

    with app.scrollPane("p1"):
        app.label("a"*200)

    with app.scrollPane("p2"):
        for i in range(500): app.label(str(i))

    app.hideScrollPaneBar("p1", "horiz")
    app.hideScrollPaneBar("p2", "horiz")
