import sys
sys.path.append("../")

from appJar import gui

with gui() as app:
    app.setFg("red")
    app.setBg("green")
    app.setFont(20)
    app.setImageLocation("images")
    app.addImage("Compound", "balloons.gif", compound="center")
