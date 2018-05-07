import sys
sys.path.append("../../")

def press(btn):
    print(btn)
    app.check("d", bg="pink")

from appJar import gui

with gui("CB Demo") as app:
    app.check("a", change=press, bg="red")
    app.check("b", over=press, fg="green")
    app.check("c", drag=press)
    app.check("d", drop=press)
    app.check("e", submit=press)
