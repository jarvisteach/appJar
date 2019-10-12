import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    app.label('hello world')
    app.image('lb', 'bStar.png')
    app.image('bStar', 'bStar.png')
    app.image('bTick', 'bStar.png')
