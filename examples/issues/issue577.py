import sys
sys.path.append("../../")

from appJar import gui

def press():
    app.setToolbarBg(app.RANDOM_COLOUR())
    try: app.addToolbarButton('z', press)
    except: pass

def enable(btn):
    if btn=='enable': app.setToolbarEnabled()
    elif btn=='disable': app.setToolbarDisabled()
    elif btn=='pin': app.setToolbarPinned()
    elif btn=='unpin': app.setToolbarPinned(False)
    elif btn=='show': app.showToolbar()
    elif btn=='hide': app.hideToolbar()

with gui() as app:
    app.label('hello world')
    app.toolbar(['a', 'b', 'c', 'd', 'e', 'f', 'save'], press, findIcon=True, pinned=False, bg='yellow')
    app.addToolbarButton('k', press)
    app.buttons(['enable', 'disable'], enable)
    app.buttons(['pin', 'unpin'], enable)
    app.buttons(['show', 'hide'], enable)
