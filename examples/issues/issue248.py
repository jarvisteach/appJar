import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.addIcon("i1", "map")
    app.addIconButton("b1", None, "map")

