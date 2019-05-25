import sys
sys.path.append("../../")

from appJar import gui

def press(): app.setEntry('e1', app.entry('New text')) 
def change():
    val = app.entry("e1")
    print('changed: ', val)
    end = val.rsplit('/', 1)[-1]
    print(end)
    app.queueFunction(app.setEntry, 'e1', end, callFunction=False)

with gui() as app:
    app.label('hello world')
    app.entry('e1', kind='file', change=change)
    app.button("press", press)
    app.entry("New text", label=True)
