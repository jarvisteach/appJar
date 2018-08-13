import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key): print(key, 'pressed')

with gui() as app:
    app.setLogLevel('trace')
    app.label('hello world')
    app.addMenuItem('a', 'a', shortcut='Control-Key-1', func=keyPress)
    app.addMenuItem('a', 'b', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('a', 'd', shortcut='Control-Shift-d', func=keyPress)
    app.addMenuItem('a', 'f', shortcut='Control-Shift-F', func=keyPress)
    app.addMenuItem('a', 'a', shortcut='Control-Shift-a', func=keyPress)
    app.addMenuItem('a', 's', shortcut='Control-Shift-s', func=keyPress)

    print('binding ctrl-shift-S')
    app.topLevel.bind_all('<Control-Shift-S>', keyPress)
    print('binding ctrl-shift-a')
    app.topLevel.bind_all('<Control-Shift-a>', keyPress)
