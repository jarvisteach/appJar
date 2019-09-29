import sys
sys.path.append("../../")

from appJar import gui
count = 0

def change(p):
    global count
    count += 1
    print(p, 'change', count)

with gui('panes') as app:
    app.label('hello world')

    # start initial pane
    with app.panedFrame("p1", change=change):
        app.label("Inside Pane 1")

        # start additional panes inside initial pane
        with app.panedFrame("p2", change=change):
            app.label("Inside Pane 2")

        with app.panedFrame("p3", change=change):
            app.label("Inside Pane 3")

    with app.panedFrame("p11", change=change):
        app.label("Inside Pane 11")
        with app.panedFrame("p21", sash=20, change=change):
            app.label("Inside Pane 21")
