import sys
sys.path.append('../../')

from appJar import gui

def press():
    app.changeOptionBox('opt', ['aaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbb'])

with gui() as app:
    with app.labelFrame("test"):
        app.setSticky('ew')
        app.option('opt', ['a','b','c','d','e'])
        app.button('press', press)
