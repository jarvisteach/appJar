import sys
sys.path.append("../../")

def subber(btn):
    if btn == "FULL SUB": app.setFullscreen("SUB")
    else: app.exitFullscreen("SUB")

def noParam(): print("No param")
def param(param): print("Param:", param)
def inL(): app.label("OVER ME", "IN ME")
def outL(): app.label("OVER ME", "OUT ME")
def inP(param): app.label("OVER PARAM", "IN " + param)
def outP(param): app.label("OVER PARAM", "OUT " + param)
def clickP(param): print("CLICK:", param)
def dropP(param): print("DROP:", param)
def clickN(): print("CLICK no param")
def dropN(): print("DROP no param")


from appJar import gui

with gui() as app:
    app.addMenuItem("MENU", "PARAM", param)
    app.addMenuItem("MENU", "NO PARAM", noParam)
    app.button("NO PARAM", noParam)
    app.button("PARAM", param)
    app.link("NO PARAM", noParam)
    app.link("PARAM", param)
    app.entry("FILE", label=True, kind="file")
    app.entry("LOWER-5", label=True, limit=5, case='lower', default='LOWER')
    app.entry("UPPER-7", label=True, limit=7, case='upper', default='UPPER')
    app.date("dp", change=noParam)
    app.date("dp2", change=param)
    app.bindKey("p", param)
    app.bindKey("n", noParam)
    app.buttons(["FULL", "EXIT"], [app.setFullscreen, app.exitFullscreen])
    app.button("SUB", app.showSubWindow, name="SHOW SUB")
    app.label("OVER ME", over=[inL, outL], drag=[clickP, dropP])
    app.label("OVER PARAM", over=[inP, outP], drag=[clickN, dropN])

    with app.subWindow("SUB"):
        app.label("HELLO")
        app.button("FULL SUB", subber)
        app.button("EXIT SUB", subber)
