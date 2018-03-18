import sys
sys.path.append("../../")
from appJar import gui

def press():
    with app.toggleFrame('tog1'):
        app.label('g')

    app.openToggleFrame('tog2')
    app.addLabel('h', 'h')
    app.stopToggleFrame()

with gui() as app:
    with app.tabbedFrame("tabs"):
        with app.tab("a"):
            with app.toggleFrame("tog1"):
                app.label('a')
                app.label('b')
                app.label('c')
            with app.toggleFrame("tog2"):
                app.label('d')
                app.label('e')
                app.label('f')
    app.button('press', press)
