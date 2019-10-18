import sys
sys.path.append("../../")

from appJar import gui

def press():
    name = app.lastFocus
    if name is None:
        print('event in main gui')
    else:
        print('event in:', name)

def shower(sub):
    print('show sub:', sub)
    app.showSubWindow(sub)

with gui() as app:
    app.label('hello world')
    app.entry('e1')
    app.button('e1', press)
    app.addButtons(['s1', 's2', 's3', 's4', 's5'], shower)

    with app.subWindow('s1', visible=False) as s1:
        app.label('s1')
        app.entry('s1')
        app.button('ss1', press)
        app.location = [200,200]
    with app.subWindow('s2', visible=False) as s2:
        app.label('s2')
        app.entry('s2')
        app.button('ss2', press)
        app.location = [300,200]
    with app.subWindow('s3', visible=False) as s3:
        app.label('s3')
        app.entry('s3')
        app.button('ss3', press)
        app.location = [400,200]
    with app.subWindow('s4', visible=False) as s4:
        app.label('s4')
        app.entry('s4')
        app.button('ss4', press)
        app.location = [500,200]
        with app.subWindow('s5', visible=False) as s4:
            app.label('s5')
            app.entry('s5')
            app.button('ss5', press)
            app.location = [600,200]
