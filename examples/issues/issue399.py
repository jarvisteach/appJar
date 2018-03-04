import sys
sys.path.append("../../")

def enter(): print("IN")
def leave(): print("OUT")
def leftClick(event):
    print("CLICK")
    print(event.x, event.y)

    print(app.MOUSE_POS_IN_WIDGET(canvas, event))

from appJar import gui
app=gui()
canvas = app.addCanvas("c1")
canvas.create_oval(10, 10, 100, 100, fill="red", outline="blue", width=3)
canvas.create_line(0, 0, 255, 255, width=5)
canvas.create_line(0, 255, 255, 0, dash=123)
app.setCanvasOverFunction("c1", [enter, leave])
canvas.bind("<Button-1>", leftClick, add="+")
app.go()
