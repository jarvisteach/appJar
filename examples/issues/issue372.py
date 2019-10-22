import sys
sys.path.append("../../")

from appJar import gui

def showPositions():
    with app.frame('f1'):
        app.removeWidgetAt(2, 2)
        app.removeWidgetAt(77, 2)

with gui("Grid Demo", "300x300", sticky="news", expand="both") as app:
    with app.frame('f1'):
        for x in range(5):
            for y in range(5):
                app.label(str(x)+str(y), row=x, column=y)
        
    app.button("PRESS", showPositions, colspan=5)
