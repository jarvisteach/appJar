import sys
sys.path.append("../../")

from appJar import gui

def hide(btn=None):
    app.visible = not app.visible
    if btn is not None: app.after(2000, hide)

with gui() as app:
    app.label("DEMO SHRINK AND GROW")
    app.button("HIDE", hide)
