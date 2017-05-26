import sys
sys.path.append("../../")

from appJar import gui


coords = {
        "America":[32, 17,242, 167],
        "South America":[126, 170,226, 292],
}

def press(area):
    app.setLabel("l1", area)

app=gui()
app.addImage("i1", "map.gif")
app.setImageMap("i1", press, coords)
app.addLabel("l1", "<click the map>")
app.go()

