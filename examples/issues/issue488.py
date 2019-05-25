import sys
sys.path.append("../../")

from appJar import gui

def menu1(): print('menu1')
def menu2(): print('menu2')
def shiftmenu1(): print('shiftmenu1')
def shiftmenu2(): print('shiftmenu2')

with gui() as app:
    app.label('hello world')
    app.label("Control - 1 - 2")
    app.bindKey('1', menu1)
    app.bindKey('<Control-Key-1>', shiftmenu1)
    app.addMenuItem('test', 'test', menu2, shortcut='2')
    app.addMenuItem('test', 'shufttest', shiftmenu2, shortcut='Control-2')
