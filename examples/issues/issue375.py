import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.editMenu = True
    app.entry("a")
    app.entry("b", kind="standard")
    app.entry("c", kind="file")
    app.entry("d", kind="numeric")
    app.entry("e", kind="directory")
    app.entry("e", kind="auto")
    app.entry("e", kind="validation")
    app.text("t1", scroll=True)
    app.text("t2", scroll=True)
    app.option("o", [1,2,3])
