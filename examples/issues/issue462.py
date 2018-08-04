import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn == 'SHOW': app.showSubWindow('Info')
    elif btn == 'EMPTY': app.emptySubWindow('Info')
    else: makeSub()

def makeSub():
    with app.subWindow('Info'):
        app.addLabel('This will crash if not empty')

with gui('Emptying Containers') as app:
    app.label('Try emptying a container')
    app.buttons(['SHOW', 'EMPTY', 'POPULATE'], press)
    makeSub()
