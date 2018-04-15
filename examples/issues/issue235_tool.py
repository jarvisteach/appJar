import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    print(btn)

with gui() as app:
    app.label('hello world')
    app.toolbar(["A", "OPEN", "CLOSE"], press, pinned=False)
