import sys
sys.path.append("../../")

data1 = ['a', 'b', 'c', 'd']
data2 = ['e', 'f', 'g', 'h']
data3 = ['i', 'j', 'k', 'l']
btns = ["get", "select", "deselect", "toggle", "clear", "rename", "replace", "add", "delete"]

from appJar import gui

def press(btn):
    print(btn)
    if btn in ["select", "delete", "deselect", "toggle"]:
        app.listbox("box", 2, mode=btn)
        app.spinbox("box", 2, mode=btn)
        app.optionbox("box", 2, mode=btn)
    elif btn == "clear":
        app.listbox("box", mode=btn)
        app.spinbox("box", mode=btn)
        app.optionbox("box", mode=btn)
    elif btn == "replace":
        app.listbox("box", data2, mode=btn)
        app.spinbox("box", data2, mode=btn)
        app.optionbox("box", data2, mode=btn)
    elif btn == "add":
        app.listbox("box", "zz", mode=btn)
        app.spinbox("box", "zz", mode=btn)
        app.optionbox("box", "zz", mode=btn)
    elif btn == "get":
        print(app.listbox("box"))
        print(app.spinbox("box"))
        print(app.optionbox("box"))

with gui(sticky="new", bg="green") as app:
    app.label('hello world', colspan=3)
    app.listbox("box", data1, pos=(1,0))
    app.spinbox("box", data1, pos=(1,1))
    app.optionbox("box", data1, pos=(1,2))
    app.separator(colspan=3)
    app.buttons(btns, press, colspan=3)
    app.tick("List", pos=(4,0))
    app.tick("Spin", pos=(4,1))
    app.tick("Option", pos=(4,2))
