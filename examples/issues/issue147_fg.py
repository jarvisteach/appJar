import sys
sys.path.append("../../")

from appJar import gui

def press():
    app.setLinkFg('press', app.RANDOM_COLOUR())
    app.setEntryFg('ent', app.RANDOM_COLOUR())
    app.setLabelFg('aaaaa', app.RANDOM_COLOUR())
    app.setLabelFg('bbbbb', app.RANDOM_COLOUR())

with gui(font=25, bg='black') as app:
    app.label('hello world')
    app.link('press', press, fg='red')
    app.entry('ent', default='type here')
    app.label('aaaaa')
    app.label('bbbbb', kind='flash')
