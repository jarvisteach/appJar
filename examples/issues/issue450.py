import sys
sys.path.append("../../")

from appJar import gui

def press(): print(app.getAllOptionBoxes())

with gui() as app:
    app.label('hello world')
    app.option("opt", [-1, -2, -3])
    app.option("opt2", [-1, -2, -3], disabled="*")
    app.option("lopt", [-1, -2, -3], label=True)
    app.option("lopt2", [-1, -2, -3], disabled="*", label=True)

    app.option("topt", [-1, -2, -3], kind="ticks")
    app.option("topt2", [-1, -2, -3], disabled="*", kind="ticks")
    app.option("tlopt", [-1, -2, -3], label=True, kind="ticks")
    app.option("tlopt2", [-1, -2, -3], disabled="*", label=True, kind="ticks")

    app.addOptionBox("ob1", [-1, -2, -3])
    app.addOptionBox("ob2", [-1, -2, -3], disabled="*")

    app.addOptionBox("ctob", [-1, -2, -3, "*a", "*b", "xa", "xb"], disabled="*")
    app.setOptionBoxDisabledChar("ctob", "x")

    app.button("click me", press)
