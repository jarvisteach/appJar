import sys
sys.path.append("../../")
from appJar import gui
from PIL import Image, ImageTk

with gui("Transparent Demo", geom="400x400", sticky="news", bg="green") as app:
    app.label("l1", "", row=0, column=0, bg="black")
    app.label("l2", "", row=0, column=1, bg="red")
    photo = ImageTk.PhotoImage(file="lb3.gif")
    app.configure(sticky="")
    app.addImageData("image", photo, fmt="PhotoImage", column=0, row=0, colspan=2)
