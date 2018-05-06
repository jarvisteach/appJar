import sys
sys.path.append("../../")

from appJar import gui

def top(btn): app.top = btn=="TOP"
def hideAll(): app.hideAllSubWindows()
def showAll(): app.showAllSubWindows()
def destroy(): app.destroySubWindow("b2")
def show():
    print(app.top)
    print(b1.attributes("-topmost"))
    print(b2.attributes("-topmost"))
    print(b3.attributes("-topmost"))

with gui("Welcome", "250x200", location="200,350", top=True) as app:
    app.message('hello world')
    app.buttons(["TOP", "NOT"], top)
    app.button("SHOW", show)
    app.button("HIDE ALL", hideAll)
    app.button("SHOW ALL", showAll)
    app.button("DESTROY", destroy)

    with app.subWindow("b1", location="200,100", size="50x200", top=False, visible=True) as b1:
        app.label("l1")
        def a(): print(b1.attributes("-topmost"))
        app.button("b1", a)
        def aa(): print(b1.attributes("-topmost", False))
        app.button("bb1", aa)

    with app.subWindow("b2", location="300,100", size="50x200", top=True, visible=True) as b2:
        app.label("l2")
        def b(): print(b2.attributes("-topmost"))
        app.button("b2", b)

    with app.subWindow("b3", location="400,100", size="50x200", top=False, visible=True) as b3:
        app.label("l3")
        def c(): print(b3.attributes("-topmost"))
        app.button("b3", c)
