import sys
sys.path.append("../../")

from appJar import gui

def showSub():
    app.showSubWindow('subber')
    print('done')

with gui() as app:
    with app.subWindow('subber', modal=True):#, blocking=True):
        app.label("bbbb")

    app.button("subber", showSub)
