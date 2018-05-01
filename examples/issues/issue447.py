import sys
sys.path.append("../../")
from appJar import gui
from appJar.appjar import AJRectangle, Point

rectangles = [
    AJRectangle("red", Point(0, 0), 50, 50)
]


def click(event):
    print(event.x, event.y)
    for rect in rectangles:
        if rect.contains(Point(event.x, event.y)):
            print(rect.name)

with gui("Canvas Click", "400x400") as app:
    app.label('hello world')
    app.addCanvas("c1").bind("<Button-1>", click)
