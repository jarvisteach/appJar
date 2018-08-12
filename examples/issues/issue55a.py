import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('left', pos=(0,0))
    app.label('right', pos=(0,1))
    app.colspan=2
    for a in range(10):
        app.label(a, bg=app.RANDOM_COLOUR())
