import sys
sys.path.append("../../")

from appJar import gui

def press():
    print("hello")
    app.listbox("box", ['v', 'n', 't'])
    app.listbox("box", 'b')

    app.spin("box", 'b')
    #app.spin("box", ['v', 'n', 't'])

with gui() as app:
    app.label('hello world')
    app.listbox("box", ['a', 'b', 'c', 'd'])
    app.spin("box", ['a', 'b', 'c', 'd'])
    app.button("press", press)
