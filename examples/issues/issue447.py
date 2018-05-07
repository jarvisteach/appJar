import sys
sys.path.append("../../")
from appJar import gui, AjRectangle, AjPoint

rectangles = [
    AjRectangle("red", AjPoint(0, 0), 50, 50)
]
coords = {
    "America":[32, 17, 70, 70],
    "South America":[120, 100, 140, 150],
}

def press(val):
    print(val)



def click(event):
    print(event.x, event.y)
    for rect in rectangles:
        if rect.contains(AjPoint(event.x, event.y)):
            print(rect.name)

with gui("Canvas Click", "400x400") as app:
    app.label('hello world')
    app.addCanvas("c1").bind("<Button-1>", click)
    app.addCanvas("c2")
    app.setCanvasMap("c2", press, coords)
