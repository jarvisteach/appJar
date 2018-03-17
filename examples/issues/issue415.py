import sys
sys.path.append("../../")

from appJar import gui

def press():
    app.disableEntry('FILES')
    ent = app.getEntryWidget('FILES')
    print(ent)
    ent.theButton.config(state='disabled')

with gui() as app:
    app.label('hello world')
    app.entry("FILES", kind='file')
    app.button('DISABLE', press)
