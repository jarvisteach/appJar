import sys
sys.path.append("../../")
import tkFont as font

from appJar import gui

with gui("This is it", "400x400", font={'size':20}) as app:
    app.label("Label 1")
    app.label("Label 2")
    app.entry("entry 1", "some text", label=True)
    app.entry("entry 2", "some text", label=True)
    app.button("PRESS", None)

    with app.labelFrame("LF1", font=font.Font(size=8, weight='bold')):
        app.label("Label 11")
        app.label("Label 22")
        app.entry("entry 11", "some text", label=True)
        app.entry("entry 22", "some text", label=True)
        app.button("PRESS1", None)
