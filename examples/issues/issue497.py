import sys
sys.path.append("../../")
from random import randint
from timeit import Timer as T

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
    with app.frame('top'):
        app.button('Accessibility', app.showAccess, icon='ACCESS')
        app.label('hello world')
    with app.tabbedFrame('tabs'):
        with app.tab('scrollpane'):
            with app.scrollPane('sp'):
                app.buttons(['PRESS', 'SASH'], [doGUI, sash])
                with app.labelFrame('lf1'):
                    app.label(str(randint(0, 100)))

                with app.panedFrame('left', sash=50) as p:
                    with app.frameStack('fs'):
                        for c in 'abcdefghijkl':
                            with app.frame(c):
                                app.label(c)
                    app.buttons(['PREV', 'NEXT'], fsBut)

                    with app.panedFrame('tr', vertical=True, sash=20) as tr:
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

        with app.tab('pages'):
            with app.pagedWindow('pages'):
                for t in range(30):
                    with app.page(): app.label('p'+str(t))
        for t in range(randint(3,7)):
            with app.tab('t'+str(t)): app.label('t'+str(t))

        with app.tab('tt'):
            app.link('here', doGUI)
            app.entry('e1', kind='file')
            app.entry('e2', kind='directory')
            app.entry('e3', kind='numeric')
            app.entry('e4', kind='auto')
            app.entry('e5', kind='validation')
            app.meter('m1')
            app.grip()
            app.separator()
            app.separator()
            app.separator()

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

with gui(location='200,200') as app:
    app.statusbar(fields=5)
    app.bg='red'
    doGUI()
    with app.tabbedFrame('tabs'):
        with app.tab('t1'): app.label('catch me')

    with app.subWindow('sub', visible=True, location='300,300'):
        app.bg='blue'
