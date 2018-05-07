import sys
sys.path.append("../../")
from appJar import gui

with gui("appJar") as app:
    app.setPadding(10, 10)
#    app.ttkStyle.configure(".", background="blue")
    app.addButton("Button", func=None)
    app.addButton("Button2", func=None)
    
    with app.frame("frame"):
        app.setPadding(10, 10)
 #       app.ttkStyle.configure(".", background="white")
        app.setBg("white")
        app.addButton("Button3", func=None)
        app.addButton("Button4", func=None)
