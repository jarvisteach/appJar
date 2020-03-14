import sys
sys.path.append("../../")

from appJar import gui

def change(val):
#    print(val,app.getToggleFrameState(val))
    return True

with gui() as app:
    app.label('hello world')
    with app.pagedWindow('pages'):
        app.setPagedWindowChangeFunction('pages', change)
        with app.page():
            with app.tabbedFrame('tf', change=change):
                with app.tab('one'):
                    with app.toggleFrame('tf', change=change):
                        app.label('a')
                        app.label('b')
                        app.label('c')
                        app.label('d')
                        app.label('e')
                with app.tab('two'): app.label('two')
        with app.page(): app.label('p2')
        with app.page(): app.label('p3')
        with app.page(): app.label('p4')

    app.setToggleFrameChangeFunction('tf', change)
