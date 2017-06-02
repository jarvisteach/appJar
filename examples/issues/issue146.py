import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)

app = gui()

app.createMenu("Menu")
app.addMenuItem("Menu", "option 1", func=press, underline=2, shortcut="ctrl-c")
app.addMenuItem("Menu", "option 2", func=press, underline=2, shortcut="option-d")
app.addMenuItem("Menu", "option 3", func=press, underline=2, shortcut="shift-e")
app.addMenuItem("Menu", "option 4", func=press, underline=2, shortcut="meta-f")
app.addMenuItem("Menu", "option 5", func=press, underline=2, shortcut="ctrl-g")
app.addMenuItem("Menu", "option 6", func=press, underline=2, shortcut="ctrl-h")

app.addLabel("l1", "Label Here")
app.go()
