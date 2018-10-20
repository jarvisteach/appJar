import sys
sys.path.append("../../")

from appJar import gui

with gui('labelframes', bg='purple') as app:
    app.label('hello world')
    with app.labelFrame('main frame', bg='yellow'):
        app.label('top', bg='red')
        app.label('bottom', bg='green')

    with app.labelFrame('2nd frame', bg='pink'):
        app.label('top again', bg='red')
        app.label('bottom again', bg='green')

    app.setLabelFramePadding('2nd frame', [20,20])
