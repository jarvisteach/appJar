import sys
sys.path.append("../../")

from appJar import gui

def change(btn):
    print(btn, "change")

def submit(btn):
    print(btn, "submit")

def drop(btn):
    print(btn, "drop")

def over(btn):
    print(btn, "over")

def press(btn):
    app.entry("e2", bg="green")
    

with gui("Entry Demo") as app:
    app.addMenuEdit()
    app.entry("e1", "focus", focus=True, bg="red", fg="green", justify="right", borderwidth=5)
    app.entry("e2", "ch-su-drop", change=change, submit=submit, drop=True)
    app.entry("e3", "over-drag", over=change, drag=change, limit=5, case="upper")
    app.entry("e4", "tooltip-menu", tooltip="hello", right=True)
    app.entry("e5", kind="numeric")
    app.entry("e7", ["a", "aa", "aab", "b", "c"], kind="auto")
    app.entry("e8", kind="file", change=change, over=over)
    app.entry("e9", kind="directory", change=change)
    app.label("l1", "hiya", focus=True, right=True)
    x = app.gr()
    app.text("t1", pos=(x, 0), change=change, drop=drop, fg="red")
    app.text("t2", scroll=True, pos=(x, 1), over=change, bg="pink")
    app.button("PRESS", press, pos=(None, 0, 2))

    app.setButtonFont(size=20, family="Times", underline=True)

