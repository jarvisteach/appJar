import sys
sys.path.append("../../")

from appJar import gui

def refillFrame():
    with app.frame('one'):
        app.removeAllWidgets(True)
    app.queueFunction(fillFrame)

def fillFrame():
    with app.frame('one'):
        with app.labelFrame("labels"):
            for x in 'abcdefghijklmnopqrstuvwxyz':
                app.label('hello'+x, bg=app.RANDOM_COLOUR())

with gui() as app:
    with app.tabbedFrame('tabs'):
        with app.tab('one'):
            fillFrame()
        with app.tab('two'):
            app.button('redo', refillFrame)
