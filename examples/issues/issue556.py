import sys
sys.path.append("../../")

from appJar import gui


def launch(win):
    app.showSubWindow(win)

def bg():
    app.removeBgImage()

with gui('main', '300x300') as app:
#    app.setBgImage('map.gif')
    app.sticky = ''
    app.stretch = 'both'

    # these go in the main window
    app.addButtons(["one", "two"], launch)
    app.entry('a')
    app.check('a')
    app.button("REMOVE", bg)

    # this is a pop-up
    with app.subWindow('one', modal=True, location='100,100'):
        app.addImage("pic", 'lb3.gif')
        app.addLabel("l1", "SubWindow One")

    # this is another pop-up
    with app.subWindow('two', '300x300', visible=True, location='150,200'):
#        app.setBgImage('lb3.gif')
        app.addLabel("l2", "SubWindow Two")

    app.showSubWindow('one')
