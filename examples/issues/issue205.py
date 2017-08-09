import sys
sys.path.append("../../")

from appJar import gui

def press(btn):
    if btn in ["fred", "b"]:
        app.setOptionBox("box", btn)
    else:
        btn = int(btn)
        if app.getCheckBox("Delete"):
            app.deleteOptionBox("box", btn)
        else:
            app.setOptionBox("box", btn)


app = gui()
app.addOptionBox("box", ["", "a", "b", "c", "d", "e"])
app.addCheckBox("Delete")
app.addButtons(["fred", "b",  "-1", "0", "1", "2", "3", "4", "5"], press)
app.go()
