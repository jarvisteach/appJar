import sys
sys.path.append("../../")

from appJar import gui

def test(): print("test")

with gui() as app:
    app.label('hello world')
    app.addToolbar(['help', 'save', 'open'], test, True)
    app.button('PRESS', test, icon='help')
