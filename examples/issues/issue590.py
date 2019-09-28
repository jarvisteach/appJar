import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.addFileEntry(title="ca")
    app.disableEntry(name="ca")
