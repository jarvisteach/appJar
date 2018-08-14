import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key): print(key, 'pressed')

with gui() as app:
    app.setLogLevel('trace')
    app.label('hello world')
    app.addMenuItem('a', '1', shortcut='Key-1', func=keyPress)
    app.addMenuItem('a', '2', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('a', '3', shortcut='Alt-Key-3', func=keyPress)
    app.addMenuItem('a', '4', shortcut='Option-Key-4', func=keyPress)
    app.addMenuItem('a', '5', shortcut='Command-Key-5', func=keyPress)
    app.addMenuItem('a', 'w', shortcut='Control-w', func=keyPress)
    app.addMenuItem('a', 'e', shortcut='Option-e', func=keyPress)
    app.addMenuItem('a', 'a', shortcut='Control-Shift-a', func=keyPress)
    app.addMenuItem('a', 's', shortcut='Control-Alt-s', func=keyPress)
    app.addMenuItem('a', 'h', shortcut='Alt-Control-h', func=keyPress)
    app.addMenuItem('a', 'd', shortcut='Alt-shift-d', func=keyPress)
    app.addMenuItem('a', 'f', shortcut='Control-Shift-f', func=keyPress)
    app.addMenuItem('a', 'g', shortcut='Control-shift-g', func=keyPress)

#    print('binding ctrl-shift-S')
#    app.topLevel.bind_all('<Control-Shift-S>', keyPress)
#    app.bindKey('<Control-Shift-E>', keyPress)
#    app.bindKey('<Control-Shift-R>', keyPress)
#    app.bindKey('<z>', keyPress)
#    app.bindKey('<Control-x>', keyPress)
