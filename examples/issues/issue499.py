import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key): print(key, 'pressed')

with gui() as app:
    app.setLogLevel('trace')
    app.label('hello world')
    app.addMenuItem('a', 'a', shortcut='Control-Key-1', func=keyPress)
    app.addMenuItem('a', 'b', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('a', 'c', shortcut='Control-Shift-t', func=keyPress)

    app.topLevel.bind_all('<Control-Shift-S>', keyPress)
    app.topLevel.bind_all('<Control-Shift-a>', keyPress)
