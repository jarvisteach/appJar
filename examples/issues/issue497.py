import sys
sys.path.append("../../")
from random import randint

from appJar import gui

def doGUI():
    app.removeAllWidgets(sub=True)
    app.button('Accessibility', app.showAccess, icon='ACCESS')
    app.label('hello world')
    app.button('PRESS', doGUI)
    with app.labelFrame('lf1'):
        app.label(str(randint(0, 100)))
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
