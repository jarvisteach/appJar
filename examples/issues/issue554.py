import sys
sys.path.append("../../")

data = [["Homer", "Simpson", "America", 40],
["Marge", "Simpson", "America", 38],
["Lisa", "Simpson", "America", 12],
["Maggie", "Simpson", "America", 4],
["Bart", "Simpson", "America", 14]]

from appJar import gui

def btnCallback(btn):
    app.deleteTabbedFrameTab("Address Book", "Homer")

with gui("Updating Labels") as app:
    with app.tabbedFrame("Address Book"):
        for pos in range(len(data)):
            with app.tab(data[pos][0]):
                app.entry(str(pos)+"fName", data[pos][0], label="First Name")
                app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
                app.entry(str(pos)+"country", data[pos][2], label="Country")
                app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")
    app.addButton("Delete", btnCallback)
