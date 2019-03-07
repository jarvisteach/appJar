import sys
sys.path.append("../../")

from appJar import gui
count = 0

def change():
    global count
    count += 1
    print('change', count)

with gui() as app:
    app.label('hello world')

    # start initial pane
    app.startPanedFrame("p1")
    app.addLabel("l1", "Inside Pane 1")

    # start additional panes inside initial pane
    app.startPanedFrame("p2")
    app.addLabel("l2", "Inside Pane 2")
    app.stopPanedFrame()

    app.startPanedFrame("p3")
    app.addLabel("l3", "Inside Pane 3")
    app.stopPanedFrame()

    # stop initial pane
    app.stopPanedFrame()

    app.setPanedFrameChangeFunction('p3', change)

    app.startPanedFrame("p11")
    app.addLabel("l11", "Inside Pane 1")
    app.startPanedFrame("p21")
    app.addLabel("l21", "Inside Pane 2")
    app.stopPanedFrame()
    app.stopPanedFrame()
