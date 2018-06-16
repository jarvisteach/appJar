import sys
sys.path.append("../../")

from appJar import gui

MENU_NAME = "Checkers"
SUB_MENU = "SubMenu"
ITEMS = ['a', 'b', 'c', 'd']

def checker(men):
    for i in ITEMS:
        print(MENU_NAME, i, app.getMenuCheckBox(MENU_NAME, i))
        print(SUB_MENU, i, app.getMenuCheckBox(SUB_MENU, i))

    # delete menu items
    app.widgetManager.get(app.Widgets.Menu, MENU_NAME).delete("d")
    app.widgetManager.remove(app.Widgets.Menu, MENU_NAME+"cb"+"d", group='vars')

    app.widgetManager.get(app.Widgets.Menu, SUB_MENU).delete("b")
    app.widgetManager.remove(app.Widgets.Menu, SUB_MENU+"cb"+"b", group='vars')

    app.widgetManager.get(app.Widgets.Menu, MENU_NAME).delete(SUB_MENU)
    app.widgetManager.remove(app.Widgets.Menu, SUB_MENU)

def press():
    app.addSubMenu(MENU_NAME, SUB_MENU)
    for i in ITEMS: app.addMenuCheckBox(SUB_MENU, i, checker)

with gui() as app:
    app.label('Menus')
    for i in ITEMS: app.addMenuCheckBox(MENU_NAME, i, checker)
    app.addSubMenu(MENU_NAME, SUB_MENU)
    for i in ITEMS: app.addMenuCheckBox(SUB_MENU, i, checker)
    app.button("ADD", press)

