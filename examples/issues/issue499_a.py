import sys
sys.path.append("../../")

from appJar import gui

def press():
    print(press)

with gui() as app:
    app.label('hello world')
    app.entry('aaa')
    app.enableEnter(press)
    app.disableEnter()
    app.enableEnter(press)
