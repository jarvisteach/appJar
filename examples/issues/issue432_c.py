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

    app.entry("First Name", data[pos][0])
    app.entry("Last Name", data[pos][1])
    app.entry("Country", data[pos][2])
    app.entry("Age", data[pos][3])

with gui("Updating Labels") as app:
    app.entry("First Name", label=True)
    app.entry("Last Name", label=True)
    app.entry("Country", label=True)
    app.entry("Age", kind='numeric', label=True)
    app.buttons(["Previous", "Next"], press)
    press("Next")
