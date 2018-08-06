import sys
sys.path.append("../../")
from random import randint

from appJar import gui

def fsBut(btn):
    if btn == "PREV": app.prevFrame('fs')
    elif btn == "NEXT": app.nextFrame('fs')

def sash():
    pos = app.integerBox('Sash Pos', 'Enter a sash position')
    if pos is not None:
        app.setPaneSashPosition(pos, 'left')
        with app.panedFrame('tr'):
            app.setPaneSashPosition(90)

def doGUI():
    app.removeAllWidgets(sub=True)
    app.button('Accessibility', app.showAccess, icon='ACCESS')
    app.label('hello world')
    with app.scrollPane('sp'):
        app.buttons(['PRESS', 'SASH'], [doGUI, sash])
        with app.labelFrame('lf1'):
            app.label(str(randint(0, 100)))

        with app.panedFrame('left', sash=50) as p:
            with app.frameStack('fs'):
                for c in 'abcdefghijkl':
                    with app.frame(c):
                        app.label(c)

            with app.panedFrameVertical('tr', sash=20) as tr:
                with app.scrollPane("PANE"):
                    for x in range(10):
                        for y in range(10):
                            name = str(x) + "-" + str(y)
                            app.label(name, row=x, column=y, bg=app.RANDOM_COLOUR())

                with app.panedFrame('br'):
                    with app.toggleFrame("Options"):
                        app.tick("Show this")
                        app.tick("Show that")
                        app.tick("Show the other")

    app.buttons(['PREV', 'NEXT'], fsBut)
    doTabs()
    soSub()

def soKill():
    app.destroyAllSubWindows()

def soSub():
    with app.subWindow('sub', visible=True, location='300,300'):
        app.removeAllWidgets(current=True)
        app.emptyCurrentContainer()
        app.label(str(randint(0, 100)))
        app.button('press', soSub)
        app.button('kill', soKill)

def doTabs():
    with app.tabbedFrame('tabs'):
        for t in range(randint(3,7)):
            with app.tab('t'+str(t)): app.label('t'+str(t))

with gui(location='200,200') as app:
    app.bg='red'
    doGUI()
    with app.tabbedFrame('tabs'):
        with app.tab('t1'): app.label('catch me')

    with app.subWindow('sub', visible=True, location='300,300'):
        app.bg='blue'
