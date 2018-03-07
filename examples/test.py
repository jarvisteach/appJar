import sys
sys.path.append("../")

from appJar import gui


def doIt(NAME):
    if NAME == 'KILL': app.destroySubWindow('sub')
    else: app.showSubWindow('sub')

with gui() as app:
    app.buttons(["KILL", "SHOW"], doIt)
    with app.subWindow("sub"):
        app.entry("e", kind='validation')
