import sys
sys.path.append("../../")
from appJar import gui

with gui("DnD Demo") as app:
    app.label("title", "Hello World", drop=True)
    app.entry("data", drop=True)
