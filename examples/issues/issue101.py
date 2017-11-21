import sys
sys.path.append("../../")
from appJar import gui

with gui("DnD Demo") as app:
    app.label("title", "Hello World", drop=True)
    app.setLabelDragSource("title")
    app.entry("data", drop=True)
    app.text("data", drop=True)
    app.image("data", "img2.gif", drop=True)
    app.message("data", drop=True)
    app.list("data", drop=True)
