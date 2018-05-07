import sys
sys.path.append("../../")
from appJar import gui

def a(press):
    print(press)

#with gui(useTtk=True) as app:
with gui() as app:
    app.addMenuEdit()
    app.removeAllWidgets()
    app.addMenuEdit()
    app.addToolbar(["A", "B", "C", "D"], a, findIcon=False)
    buttons = app.widgetManager.group(app.Widgets.Toolbar)
    app.ttkStyle.configure("TB.TButton", background="blue", foreground="yellow")
    for button in buttons:
#        buttons[button].config(bg="red")
        buttons[button].config(style="TB.TButton")
    app.entry("a")
