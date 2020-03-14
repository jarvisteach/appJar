import sys
sys.path.append("../../")

from appJar import gui

def change(val):
    print(val,app.getToggleFrameState(val))

with gui() as app:
    app.label('hello world')
    with app.pagedWindow('pages'):
        with app.page():
            with app.tabbedFrame('tf', change=change):
                with app.tab('one'):
                    with app.toggleFrame('tf', change=change):
                        app.label('a')
                        app.label('b')
                        app.label('c')
                        app.label('d')
                        app.label('e')
                with app.tab('two'): pass
        with app.page(): pass
        with app.page(): pass
        with app.page(): pass

#    app.setToggleFrameChangeFunction('tf', change)
