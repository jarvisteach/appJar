import sys
sys.path.append("../../")
from appJar import gui
from PIL import Image, ImageTk

with gui("Transparent Demo", geom="400x400", sticky="news") as app:
    app.addCanvas("c1")
    app.addCanvasRectangle("c1", 0, 0, 200, 400, fill="black")
    app.addCanvasRectangle("c1", 200, 0, 200, 400, fill="red")
    app.addCanvasImage("c1", 200, 200, ImageTk.PhotoImage(file="lb3.gif"))
    app.addCanvasImage("c1", 100, 100, "lb3.gif")
