import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    with app.labelFrame('demo'):
        app.stretch='none'
        app.label('this one')
        app.label('this two')
        app.label('this three')
