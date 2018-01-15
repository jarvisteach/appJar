import sys
sys.path.append("../../")
from appJar import gui

def motion(event):
    app.label("pos", str(event.x)+":"+str(event.y))

with gui("Show Position", "600x600") as app:
    app.topLevel.bind('<Motion>', motion)
    app.label("pos")
