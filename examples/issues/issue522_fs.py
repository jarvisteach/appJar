import sys
sys.path.append("../../")

from appJar import gui 

def nav(btn):
    if btn == "FIRST": app.firstFrame("Pages")
    elif btn == "NEXT": app.nextFrame("Pages")
    elif btn == "PREV": app.prevFrame("Pages")
    elif btn == "LAST": app.lastFrame("Pages")

def verify():
    # return False if you want to stop the user progressing
    return True

with gui("My Paged Window", '300x500', labelFont=16, bg='black') as app:

    with app.frameStack("Pages", start=0, change=verify):
        for i in range(10):
            with app.frame():
                app.label(i, bg=app.RANDOM_COLOUR())

    app.config(sticky='esw', stretch='column')

    with app.frame('buttons'):
        app.button('FIRST', nav, icon='arrow-1-backward', pos=(0, 0), tip='First')
        app.button('PREV', nav, icon='arrow-1-left', pos=(0, 1), tip='Previous')
        app.button('NEXT', nav, icon='arrow-1-right', pos=(0, 2), tip='Next')
        app.button('LAST', nav, icon='arrow-1-forward', pos=(0, 3), tip='Last')
