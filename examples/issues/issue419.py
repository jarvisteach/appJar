import sys
sys.path.append("../../")
from appJar import gui

def press():
    with app.toggleFrame('tog1'):
        app.label('d')

with gui() as app:
    with app.tabbedFrame("tabs"):
        with app.tab("a"):
            with app.toggleFrame("tog1"):
                app.label('a')
                app.label('b')
                app.label('c')
    app.button('press', press)
