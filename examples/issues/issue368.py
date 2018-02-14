import sys
sys.path.append("../../")
from Tkinter import PhotoImage

from appJar import gui
with gui("DEMO", "300x300") as app:
#    app.label("DEMO")
    img = PhotoImage(file="map.gif")
    app.appWindow.create_image(50, 10, image=PhotoImage(file="map.gif"), anchor="nw")
    app.appWindow.img = img
