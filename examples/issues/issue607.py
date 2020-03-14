import sys
sys.path.append("../../")

from appJar import gui

def up():
    print('raising', app.option('raise'))
    app.raiseLabel(app.option('raise'))

def down():
    print('lowering', app.option('lower'))
    app.lowerLabel(app.option('lower'))

with gui() as app:
    app.label('hello world')
    vals = []
    for i in range(10):
        vals.append('i'+str(i))
        app.label(vals[i], vals[i], 1,0) 
    app.option('raise', vals, change=up, label=True)
    app.option('lower', vals, change=down, label=True)
