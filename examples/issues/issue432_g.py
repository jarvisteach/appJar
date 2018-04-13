import sys
sys.path.append("../../")

from appJar import gui

data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]


def press(btn):
    if btn == "Next": app.nextFrame("address book")
    elif btn == "Previous": app.prevFrame("address book")

    if app.frameStackAtStart("address book"):
        app.disableButton("Previous")
    elif app.frameStackAtEnd("address book"):
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

with gui("Updating Labels") as app:
    with app.frameStack("address book", start=0):
        for loop in range(len(data)):
            with app.frame():
                app.entry(str(loop)+"fName", data[loop][0], label="First Name")
                app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
                app.entry(str(loop)+"country", data[loop][2], label="Country")
                app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")

    app.buttons(["Previous", "Next"], press)
    app.disableButton("Previous")
