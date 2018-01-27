import sys
sys.path.append("../")

def press(a):
    print(a)
    app.meter("m", 20, bg="yellow")

from appJar import gui

with gui(size=(200,500), sticky="news") as app:
    app.message("m", width=20, bg="red", over=press, pos=(0,0))
    app.text("a", "asasas", change=press, row=0, column=1)
    app.link("a", "http://www.goog.e.com", tooltip="google")
    app.link("b", press, bg="green")
    app.spin("a", [1, 2, 3, 4,5], colspan=2, change=press)
    app.spin("b", [1, 2, 3, 4,5], colspan=2, change=press, label=True, bg="pink")
    app.option("f", [1, 2, 3, 4,5], colspan=2, change=press, label=True, bg="green")
    app.slider("a")
    app.meter("m", 45, column=2, bg="red", over=press)
