import sys
sys.path.append("../../")

def menu(btn): print(btn)

from appJar import gui

with gui("Menu Test") as app:
    app.label("title", "Menu Test")
    app.createMenu("Lets")
    app.addMenuItem("Lets", "One", menu, shortcut="Control-a")
    app.addMenuItem("Lets", "Two", menu, shortcut="Control-Shift-a")
    app.addMenuItem("Lets", "Three", menu, shortcut="Shift-Control-a")
    app.addMenuItem("Lets", "Four", menu, shortcut="Alt-Shift-a")
    app.addMenuItem("Lets", "Five", menu, shortcut="Shift-Alt-a")

    app.createMenu("Nums")
    app.addMenuItem("Nums", "1", menu, shortcut="Control-1")
    app.addMenuItem("Nums", "2", menu, shortcut="Control-2")
    app.addMenuItem("Nums", "3", menu, shortcut="Control-3")
    app.addMenuItem("Nums", "4", menu, shortcut="Control-4")
    app.addMenuItem("Nums", "5", menu, shortcut="Control-5")
    app.addMenuItem("Nums", "Two", menu, shortcut="Control-Shift-1")
    app.addMenuItem("Nums", "Three", menu, shortcut="Shift-Control-1")
    app.addMenuItem("Nums", "Four", menu, shortcut="Alt-Shift-1")
    app.addMenuItem("Nums", "Five", menu, shortcut="Shift-Alt-1")

    app.addMenuItem("Punct", "!", menu, shortcut="Ctrl-!")
