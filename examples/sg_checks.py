import sys
sys.path.append("../")
from appJar import gui

def press():
    print(1)
    app.check("Apples", True, bg="pink")

with gui(font=20, bg="yellow") as app:

    app.check("Apples", width=10)
    app.check("Pears", bg="green", fg="red", font=40)
    app.check("Oranges", True)
    app.check("Kiwis", change=press, width=40)
    app.button("PRESS", press)
