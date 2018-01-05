import sys
sys.path.append("../../")

def press(b):
    s = app.getTurtleScreen("t1")
    t = app.getTurtle("t1")
    s.bgcolor("green")
    for i in range(20):
        t.forward(i * 10)
        t.right(144)

from appJar import gui
app=gui()
app.addTurtle("t1")
canvas = app.addCanvas("c1")
canvas.create_oval(10, 10, 100, 100, fill="red", outline="blue", width=3)
canvas.create_line(0, 0, 255, 255, width=5)
canvas.create_line(0, 255, 255, 0, dash=123)
app.addButton("DRAW", press)
app.go()
