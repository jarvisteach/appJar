import sys
sys.path.append("../../")

from appJar import gui

with gui("EDITOR", "400x400", bg="red", fg="white", stretch="column") as app:
    app.label('Text Editor')

    app.stretch = "both"
    app.text("editor")

    app.stretch = "column"
    app.sticky = "e"
    app.check("ed1")
    app.entry("ed1")
