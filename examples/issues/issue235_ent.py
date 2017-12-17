import sys
sys.path.append("../../")

from appJar import gui

def change(btn):
    print(btn, "change")

def submit(btn):
    print(btn, "submit")

def drop(btn):
    print(btn, "drop")

def press(btn):
    app.entry("e2", bg="green")
    

with gui("Entry Demo") as app:
    app.addMenuEdit()
    app.entry("e1", "focus", focus=True, bg="red", fg="green", justify="right", borderwidth=5)
    app.entry("e2", "ch-su-drop", change=change, submit=submit, drop=True)
    app.entry("e3", "over-drag", over=change, drag=change, limit=5, case="upper")
    app.entry("e4", "tooltip-menu", tooltip="hello", menu=True)
    app.entry("e5", kind="numeric")
    app.entry("e7", ["a", "aa", "aab", "b", "c"], kind="auto")
    app.entry("e8", kind="file", change=change, over=change)
    app.entry("e9", kind="directory", change=change)
    app.label("l1", "hiya", focus=True, menu=True)
    x = app.gr()
    app.text("t1", column=0, row=x, change=change, drop=drop, fg="red")
    app.text("t2", scroll=True, column=1, row=x, over=change, bg="pink")
    app.button("PRESS", press)

    app.setButtonFont(20, ("Times", "20", "underline"))

