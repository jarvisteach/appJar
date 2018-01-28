import sys
sys.path.append("../../")
from appJar import gui
from PIL import Image, ImageTk

with gui("Transparent Demo", geom="400x400", sticky="news") as app:
    canvas = app.addCanvas("c1")
    app.addCanvasRectangle("c1", 0, 0, 200, 400, fill="black")
    app.addCanvasRectangle("c1", 200, 0, 200, 400, fill="red")
    photo = ImageTk.PhotoImage(file="lb3.gif")
    canvas.create_image(200, 200, image=photo)
