import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key):
    print(key, 'pressed')
    if key.isnumeric():
        print('numeric')

with gui() as app:
    app.label('hello world')
    app.addMenuItem('a', 'a', shortcut='Control-Key-1', func=keyPress)
    app.addMenuItem('a', 'b', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('a', 'c', shortcut='Control-Shift-T', func=keyPress)
    app.addMenuItem('a', 'd', shortcut='Control-3', func=keyPress)
    app.addMenuItem('a', 'e', shortcut='Control-Key-4', func=keyPress)
