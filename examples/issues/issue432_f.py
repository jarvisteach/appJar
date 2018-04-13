import sys
sys.path.append("../../")

from appJar import gui

data = [["Homer", "Simpson", "America", 40],
        ["Marge", "Simpson", "America", 38],
        ["Lisa", "Simpson", "America", 12],
        ["Maggie", "Simpson", "America", 4],
        ["Bart", "Simpson", "America", 14]]

pos = -1

def press(btn):
    global pos 
    if btn == "Next": pos += 1
    elif btn == "Previous": pos -= 1

    if pos == 0:
        app.disableButton("Previous")
    elif pos == len(data)-1:
        app.disableButton("Next")
    else:
        app.enableButton("Previous")
        app.enableButton("Next")

    app.raiseFrame(str(pos))



with gui("Updating Labels") as app:
    for loop in range(len(data)):
        with app.frame(str(loop), 0, 0):
            app.entry(str(loop)+"fName", data[loop][0], label="First Name")
            app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
            app.entry(str(loop)+"country", data[loop][2], label="Country")
            app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")

    app.buttons(["Previous", "Next"], press)
    press("Next")
