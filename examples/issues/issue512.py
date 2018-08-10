import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn, "pressed")
    app.setMenuCheckBox("CHECKS", btn)

with gui() as app:
    app.label('hello world')
    app.addMenuCheckBox("CHECKS", "A", press, "Ctrl-d")
