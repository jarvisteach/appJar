import sys
sys.path.append("../../")

def changeColour():
    app.label("DEMO", bg=app.colourBox())
    app.label("DEMO", app.getLabelWidget("DEMO").cget("bg"))

from appJar import gui
with gui("Colours", "400x400", sticky="news") as app:
    app.label("DEMO", submit=changeColour)
