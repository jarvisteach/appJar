import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)
    if btn == 'ADD':
        with app.tabbedFrame('tabs'):
            with app.tab('b'):
                app.addLabel('iiiiiHello World b')
                app.addLabel('Hello World b')
    elif btn == 'SHOW':
        app.setTabbedFrameSelectedTab('tabs', 'b')
    elif btn == 'DELETE':
        app.deleteTabbedFrameTab('tabs', 'b')

with gui() as app:
    with app.tabbedFrame('tabs'):
        with app.tab('a'):
            app.label('Hello World a')
        with app.tab('b'):
            app.label('Hello World b')
        with app.tab('c'):
            app.label('Hello World c')
        with app.tab('d'):
            app.label('Hello World d')


    app.buttons(['ADD', 'SHOW', 'DELETE'], press)
