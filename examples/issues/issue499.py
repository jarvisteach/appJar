import sys
sys.path.append("../../")

from appJar import gui

def keyPress(key): print(key, 'pressed')

def press(btn):
    if btn == 'ENABLE': app.enableMenuItem('a', 'w')
    elif btn == 'DISABLE': app.disableMenuItem('a', 'w')
    elif btn == 'DELETE': app.deleteMenuItem('a', 'w')

def pressm(btn):
    if btn == 'ENABLEM': app.enableMenu('a')
    elif btn == 'DISABLEM': app.disableMenu('a')
    elif btn == 'DELETEM': app.deleteMenu('a')

def pressb(btn):
    if btn == 'ENABLEB': app.enableMenubar()
    elif btn == 'DISABLEB': app.disableMenubar()
    elif btn == 'DELETEB': app.deleteMenubar()

with gui() as app:
    app.setLogLevel('trace')
    app.label('hello world')
    app.addMenuItem('b', '1', shortcut='Key-1', func=keyPress)
    app.addMenuItem('b', '2', shortcut='Control-Key-2', func=keyPress)
    app.addMenuItem('b', '3', shortcut='Alt-Key-3', func=keyPress)
    app.addMenuItem('b', '4', shortcut='Option-Key-4', func=keyPress)
    app.addMenuItem('a', '5', shortcut='Command-Key-5', func=keyPress)
    app.addMenuItem('a', 'w', shortcut='Control-w', func=keyPress)
    app.addMenuItem('a', 'e', shortcut='Option-e', func=keyPress)
    app.addMenuItem('a', 'a', shortcut='Control-Shift-a', func=keyPress)
    app.addMenuItem('a', 's', shortcut='Control-Alt-s', func=keyPress)
    app.addMenuItem('a', 'h', shortcut='Alt-Control-h', func=keyPress)
    app.addMenuItem('a', 'd', shortcut='Alt-shift-d', func=keyPress)
    app.addMenuItem('a', 'f', shortcut='Control-Shift-f', func=keyPress)
    app.addMenuItem('a', 'g', shortcut='Control-shift-g', func=keyPress)
    app.addMenuItem('c', 'u', shortcut='Shift-u', func=keyPress)
    app.addMenuItem('c', 'r', shortcut='r', func=keyPress)
    app.addMenuItem('c', 'U', shortcut='u', func=keyPress)

#    print('binding ctrl-shift-S')
#    app.topLevel.bind_all('<Control-Shift-S>', keyPress)
#    app.bindKey('<Control-Shift-E>', keyPress)
#    app.bindKey('<Control-Shift-R>', keyPress)
#    app.bindKey('<z>', keyPress)
#    app.bindKey('<Control-x>', keyPress)

    app.addButtons(['DISABLE', 'ENABLE','DELETE'], press)
    app.addButtons(['DISABLEM', 'ENABLEM','DELETEM'], pressm)
    app.addButtons(['DISABLEB', 'ENABLEB','DELETEB'], pressb)
