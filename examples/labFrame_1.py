import sys
sys.path.append('../')

from appJar import gui

with gui() as app:

    with app.labelFrame("Login Details", sticky='ew', font={'size':20}):
        app.label("Name", pos=(0, 0))
        app.entry("Name", pos=(0, 1))
        app.label("Password", pos=(1, 0))
        app.entry("Password", pos=(1, 1))
        app.buttons(["Submit", "Cancel"], None, pos=(2, 0, 2))
