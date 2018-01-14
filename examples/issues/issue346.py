import sys
sys.path.append("../../")
from appJar import gui

def a(press):
    print(press)

with gui() as app:
    app.addMenuEdit()
    app.removeAllWidgets()
    app.addMenuEdit()
    app.addToolbar(["A", "B", "C", "D"], a, findIcon=False)
    buttons = app.widgetManager.group(app.Widgets.Toolbar)
    for button in buttons:
        buttons[button].config(bg="red")
    app.entry("a")
