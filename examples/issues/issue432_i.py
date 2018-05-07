import sys
sys.path.append("../../")

from appJar import gui

data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]

def showCharacter(btn):
    for pos in range(len(data)):
        if data[pos][0] == btn:
            app.removeAllWidgets()
            makeCharacter(pos)

def makeCharacter(pos):
    with app.frame("character", 0, 0):
        app.entry("fName", data[pos][0], label="First Name")
        app.entry("lName", data[pos][1], label="Last Name")
        app.entry("country", data[pos][2], label="Country")
        app.entry("age", data[pos][3], kind='numeric', label="Age")
    app.buttons([d[0] for d in data], showCharacter)
    
with gui("Updating Labels") as app:
    makeCharacter(0)
