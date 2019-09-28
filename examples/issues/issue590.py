import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn == 'ENABLE':
        app.enableEntry(name="ca")
    else:
        app.disableEntry(name="ca")

with gui() as app:
    app.addFileEntry(title="ca")
    app.buttons(['ENABLE', 'DISABLE'], press)
