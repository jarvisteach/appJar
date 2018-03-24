import sys
sys.path.append("../../")

from appJar import gui

def press(but):
    if but == 'DISABLE': app.disableEntry('FILES')
    elif but == 'ENABLE': app.enableEntry('FILES')
    ent = app.getEntryWidget('FILES')

with gui() as app:
    app.label('hello world')
    app.entry("FILES", kind='file')
    app.buttons(['DISABLE', 'ENABLE'], press)
