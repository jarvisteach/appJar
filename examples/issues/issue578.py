import sys
sys.path.append("../../")

from appJar import gui

def press():
    print(app.getAllCheckBoxes())
    app.setCheckBoxText('number 3', 'new 3 text')
    app.check('number 1', text='new number 1')

with gui() as app:
    app.label('hello world')
    app.addCheckBox("number 1")
    app.addNamedCheckBox("2 title", "number 2")
    app.check('number 3')
    app.check('number 4', text='4 title')
    app.separator()
    app.button('PRESS', press)
