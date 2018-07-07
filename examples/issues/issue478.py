import sys
sys.path.append("../../")

from appJar import gui

with gui() as app:
    with app.labelFrame("framer"):
        app.label('hello world')

    with app.labelFrame("framer"):
        app.label('hhello world')
