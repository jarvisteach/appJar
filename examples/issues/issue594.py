import sys
sys.path.append("../../")

from appJar import gui

def showsub(win):
    app.showSubWindow(win)

with gui("ISSUE WITH AUTO-ENTRY", "350x150") as app:
    app.padding = (10,10)
    app.entry('entry1', kind='auto', value=['a1', 'b1', 'c1'], label=True, focus=True)

    with app.subWindow('sub1', modal=True):
        app.size = (300, 200)
        with app.frame('subwindowframe'):
            with app.tabbedFrame('tf'):
                with app.tab('a'):
                    app.entry('subwindowentry', ['a2', 'b2', 'c2'], kind='auto', label=True)

                with app.subWindow('sub2', modal=True, height=100):
                    app.entry('subwindowentry2', ['a2', 'b2', 'c2'], kind='auto', label=True)

    app.buttons(['sub1', 'sub2'], showsub)
