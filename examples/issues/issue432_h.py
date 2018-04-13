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
            app.showFrame(str(pos))
        else:
            app.hideFrame(str(pos))
    
with gui("Updating Labels") as app:
    for loop in range(len(data)):
        with app.frame(str(loop)):
            app.entry(str(loop)+"fName", data[loop][0], label="First Name")
            app.entry(str(loop)+"lName", data[loop][1], label="Last Name")
            app.entry(str(loop)+"country", data[loop][2], label="Country")
            app.entry(str(loop)+"age", data[loop][3], kind='numeric', label="Age")
        app.hideFrame(str(loop))

    app.buttons([d[0] for d in data], showCharacter)
    showCharacter("Homer")
