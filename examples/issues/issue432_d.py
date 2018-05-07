import sys
sys.path.append("../../")

from appJar import gui

data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]

with gui("Updating Labels") as app:
    with app.pagedWindow("Address Book"):
        for pos in range(len(data)):
            with app.page():
                app.entry(str(pos)+"fName", data[pos][0], label="First Name")
                app.entry(str(pos)+"lName", data[pos][1], label="Last Name")
                app.entry(str(pos)+"country", data[pos][2], label="Country")
                app.entry(str(pos)+"age", data[pos][3], kind='numeric', label="Age")
